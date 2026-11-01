"""Make the Listen audio: each page read by Paradee's af_heart voice, stored in GitHub releases.

Runs on GitHub Actions before build.py. For every page whose speech text changed
since its audio was made, it synthesizes the speech, encodes it as Opus in WebM
with ffmpeg, and uploads it to one of 16 releases, audio-0 to audio-f (GitHub
allows 1,000 files per release, so 16 hold 16,000 pages). The manifest, a map of
page path to {hash, url, seconds}, lives in the release audio-index, and a copy
is written for build.py.

Usage: python3 _tools/audio.py --manifest-out audio.json [--max 150] [--minutes 300]
Needs: GITHUB_TOKEN and GITHUB_REPOSITORY in the environment, ffmpeg, otterwiki,
paradee and soundfile. Without a token it only downloads the manifest (read-only).
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import Site, render  # noqa: E402
from speech import speech_blocks, speech_hash  # noqa: E402
from wikilib import CONFIG, discover  # noqa: E402

API = "https://api.github.com"
REPO = os.environ.get("GITHUB_REPOSITORY", CONFIG["repo"])
TOKEN = os.environ.get("GITHUB_TOKEN", "")
INDEX_TAG = "audio-index"
PAUSE_TEXT, PAUSE_HEADING = 0.45, 0.8


def gh(method, url, data=None, headers=None, raw=False):
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    h.update(headers or {})
    if isinstance(data, (dict, list)):
        data = json.dumps(data).encode()
        h["Content-Type"] = "application/json"
    req = urllib.request.Request(url if url.startswith("http") else API + url, data=data, headers=h, method=method)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
                return body if raw else (json.loads(body) if body else None)
        except urllib.error.HTTPError as e:
            if e.code in (404, 422) or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(2 ** attempt)


def release(tag, create=True):
    try:
        return gh("GET", f"/repos/{REPO}/releases/tags/{tag}")
    except urllib.error.HTTPError as e:
        if e.code != 404 or not create:
            return None
    return gh("POST", f"/repos/{REPO}/releases", {
        "tag_name": tag, "name": f"Listen audio ({tag})", "prerelease": True, "make_latest": "false",
        "body": "Made by _tools/audio.py. Files here are the wiki's Listen audio; don't edit by hand."})


def assets(rel):
    out, page = {}, 1
    while True:
        batch = gh("GET", f"/repos/{REPO}/releases/{rel['id']}/assets?per_page=100&page={page}")
        for a in batch:
            out[a["name"]] = a
        if len(batch) < 100:
            return out
        page += 1


def upload(rel, existing, name, data, ctype):
    if name in existing:
        gh("DELETE", f"/repos/{REPO}/releases/assets/{existing[name]['id']}")
    url = f"https://uploads.github.com/repos/{REPO}/releases/{rel['id']}/assets?name={name}"
    a = gh("POST", url, data=data, headers={"Content-Type": ctype})
    existing[name] = a
    return a


def load_manifest():
    rel = release(INDEX_TAG, create=False)
    if not rel:
        return {}
    a = next((x for x in rel.get("assets", []) if x["name"] == "audio.json"), None)
    if not a:
        return {}
    url = f"https://github.com/{REPO}/releases/download/{INDEX_TAG}/audio.json"
    try:
        return json.loads(urllib.request.urlopen(url, timeout=60).read())
    except Exception:  # fall back to the API download
        return json.loads(gh("GET", a["url"], headers={"Accept": "application/octet-stream"}, raw=True))


def synthesize(tts, blocks, wav_path):
    import numpy as np
    import soundfile as sf
    from paradee import SAMPLE_RATE
    parts = []
    for kind, text in blocks:
        audio = tts(text, voice=CONFIG["voice"])
        parts.append(np.asarray(audio, dtype=np.float32).reshape(-1))
        parts.append(np.zeros(int(SAMPLE_RATE * (PAUSE_HEADING if kind == "heading" else PAUSE_TEXT)), dtype=np.float32))
    audio = np.concatenate(parts) if parts else np.zeros(SAMPLE_RATE, dtype=np.float32)
    peak = float(np.max(np.abs(audio))) or 1.0
    audio = audio * min(1.0, 0.89 / peak)
    sf.write(wav_path, audio, SAMPLE_RATE)
    return len(audio) / SAMPLE_RATE


def encode(wav_path, out_path):
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav_path), "-ac", "1",
                    "-c:a", "libopus", "-b:a", CONFIG["audio_bitrate"], "-application", "voip",
                    "-metadata", "artist=Paradee af_heart", str(out_path)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest-out", default="audio.json")
    ap.add_argument("--max", type=int, default=150, help="most pages to voice in one run")
    ap.add_argument("--minutes", type=float, default=300, help="stop starting new pages after this long")
    args = ap.parse_args()
    start = time.time()

    manifest = load_manifest()
    print(f"manifest: {len(manifest)} pages with audio")
    if not TOKEN:
        Path(args.manifest_out).write_text(json.dumps(manifest))
        print("no GITHUB_TOKEN: read-only, nothing made")
        return

    pages = discover()
    site = Site(pages)
    todo = []
    for page in pages:
        html, _ = render(page, site)
        blocks = speech_blocks(html)
        h = speech_hash(blocks, CONFIG["voice"], CONFIG["paradee_version"])
        if manifest.get(page.path, {}).get("hash") != h and blocks:
            todo.append((page, blocks, h))
    gone = [p for p in manifest if p not in {pg.path for pg in pages}]
    print(f"to voice: {len(todo)}; removed pages: {len(gone)}")

    releases, existing = {}, {}

    def shard_of(path):
        name = hashlib.sha1(path.encode()).hexdigest()[:24]
        return name[0], name + ".webm"

    def rel_for(shard):
        if shard not in releases:
            releases[shard] = release(f"audio-{shard}")
            existing[shard] = assets(releases[shard])
        return releases[shard]

    for path in gone:
        shard, name = shard_of(path)
        rel_for(shard)
        if name in existing[shard]:
            gh("DELETE", f"/repos/{REPO}/releases/assets/{existing[shard][name]['id']}")
        manifest.pop(path, None)

    made = 0
    if todo:
        from paradee import Paradee
        tts = Paradee(version=CONFIG["paradee_version"], threads=max(1, os.cpu_count() or 1))
        with tempfile.TemporaryDirectory() as tmp:
            for page, blocks, h in todo:
                if made >= args.max or (time.time() - start) / 60 > args.minutes:
                    print(f"stopping: {len(todo) - made} pages left for the next run")
                    break
                try:
                    wav, webm = Path(tmp) / "a.wav", Path(tmp) / "a.webm"
                    seconds = synthesize(tts, blocks, wav)
                    encode(wav, webm)
                    shard, name = shard_of(page.path)
                    rel = rel_for(shard)
                    upload(rel, existing[shard], name, webm.read_bytes(), "audio/webm")
                    manifest[page.path] = {
                        "hash": h, "seconds": round(seconds),
                        "url": f"https://github.com/{REPO}/releases/download/audio-{shard}/{name}"}
                    made += 1
                    print(f"voiced {page.path} ({round(seconds)} s)")
                except Exception as e:  # one bad page shouldn't stop the rest
                    print(f"warning: {page.path}: audio failed: {e}", file=sys.stderr)

    if made or gone:
        idx = release(INDEX_TAG)
        upload(idx, assets(idx), "audio.json", json.dumps(manifest, indent=0).encode(), "application/json")
    Path(args.manifest_out).write_text(json.dumps(manifest))
    print(f"done: {made} voiced in {round((time.time() - start) / 60, 1)} min")


if __name__ == "__main__":
    main()
