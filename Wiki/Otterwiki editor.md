# Otterwiki editor

Otterwiki is the wiki editor. It runs in a container on Mikey's Fedora laptop and works on a copy of the GitHub repo: every save becomes a commit that it pushes to GitHub, and it pulls from GitHub once a minute, so pages Claude writes appear in it within a minute or two. Only the laptop can reach it, at `http://localhost:8080`.

The setup files are `_tools/editor/compose.yaml` and `_tools/editor/env.example` in the repo.

## First-time setup

1. Make a GitHub token. On GitHub, open Settings, then Developer settings, Personal access tokens, Fine-grained tokens, and Generate new token. Name it "Otterwiki", choose the longest expiration offered, and under Repository access choose Only select repositories and pick `nowmichaelclark/wiki`. Under Permissions, set Contents to Read and write. Generate it and copy it.
2. Install the compose tool, once: `sudo dnf install podman-compose`
3. Make a folder and fetch the two setup files:

```sh
mkdir -p ~/wiki-editor && cd ~/wiki-editor
curl -fsSLO https://raw.githubusercontent.com/nowmichaelclark/wiki/main/_tools/editor/compose.yaml
curl -fsSL -o .env https://raw.githubusercontent.com/nowmichaelclark/wiki/main/_tools/editor/env.example
```

4. Open `.env` in a text editor (`nano .env`), paste the token after `GITHUB_TOKEN=`, and save.
5. Start it: `podman compose up -d`. The first start downloads Otterwiki and the wiki, which takes a minute.
6. Open `http://localhost:8080`, choose Register, and make an account. The first account is the admin, and only signed-in accounts can edit.
7. To have it start by itself after a reboot: `systemctl --user enable --now podman-restart.service`

## Everyday use

- Edit and save as normal. The change is on GitHub a few seconds later, and on the website a few minutes after that.
- Upload images, audio and other files with the Attachments button on a page. They are committed with the page.
- To stop it: `cd ~/wiki-editor && podman compose down`. Nothing is lost; the wiki is on GitHub and in a podman volume.
- To update Otterwiki: `cd ~/wiki-editor && podman compose pull && podman compose up -d`.

## When something goes wrong

- **A page I just saved isn't on GitHub.** The push failed, usually because GitHub had a newer change. The next sync, within a minute, merges the two and pushes. If the same lines were changed in both places, the sync can't merge them: it stops, and `podman compose logs` says "pull failed". Copy your version of the page into a text file, start over (below), and paste it back in.
- **"Permission denied" or "Authentication failed" in the logs.** The token has expired or lacks Contents: Read and write. Make a new one, put it in `.env`, and run `podman compose up -d` again.
- **Start over completely:** `podman compose down -v` deletes the local copy and the account, and the next `podman compose up -d` clones the wiki again from GitHub.
