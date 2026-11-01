// The only script on every page: search, the Listen player, and the 404 redirect.
(function () {
  "use strict";
  var BASE = "__BASE__";

  // ---- 404: Otterwiki-style addresses (/Background/Seeded%20randomness) to site ones
  if (window.WIKI_404) {
    var p = decodeURIComponent(location.pathname);
    if (p.indexOf(BASE) === 0) p = p.slice(BASE.length); else p = p.replace(/^\//, "");
    var nonWord;
    try { nonWord = new RegExp("[^\\p{L}\\p{N}_]+", "gu"); } catch (e) { nonWord = /[^a-z0-9_]+/g; }
    var slug = p.replace(/\.md$/i, "").split("/").filter(Boolean).map(function (s) {
      return s.toLowerCase().replace(nonWord, "-").replace(/^[-_]+|[-_]+$/g, "");
    }).join("/");
    var target = BASE + (slug && slug !== "home" ? slug + "/" : "");
    if (target !== location.pathname && !sessionStorageGet("tried:" + target)) {
      sessionStorageSet("tried:" + target, "1");
      location.replace(target + location.hash);
    }
  }
  function sessionStorageGet(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } }
  function sessionStorageSet(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }

  // ---- Listen
  var bar = document.querySelector(".listen");
  if (bar) {
    var audio = bar.querySelector("audio"), btn = bar.querySelector(".listen-btn"), speed = bar.querySelector(".speed");
    var saved = 1;
    try { saved = parseFloat(localStorage.getItem("wiki-speed")) || 1; } catch (e) {}
    speed.value = String(saved);
    btn.addEventListener("click", function () {
      bar.classList.add("on");
      audio.hidden = false; speed.hidden = false;
      audio.playbackRate = saved;
      audio.play();
      if ("mediaSession" in navigator) {
        navigator.mediaSession.metadata = new MediaMetadata({ title: bar.getAttribute("data-title"), artist: document.title.split(" - ").pop() });
      }
    });
    audio.addEventListener("loadedmetadata", function () { audio.playbackRate = saved; });
    speed.addEventListener("change", function () {
      saved = parseFloat(speed.value) || 1;
      audio.playbackRate = saved;
      try { localStorage.setItem("wiki-speed", String(saved)); } catch (e) {}
    });
  }

  // ---- Search: titles, headings and summaries, loaded on first use
  var form = document.querySelector(".search"), input = form && form.querySelector("input"), box = form && form.querySelector(".results");
  var data = null, loading = null;
  function load() {
    if (data) return Promise.resolve(data);
    if (!loading) loading = fetch(BASE + "search.json").then(function (r) { return r.json(); }).then(function (d) { data = d; return d; });
    return loading;
  }
  function norm(s) { return (s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, ""); }
  function search(q) {
    var words = norm(q).split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    var hits = [];
    data.forEach(function (d) {
      var t = norm(d.t), h = norm(d.h.join(" ")), s = norm(d.s), score = 0;
      for (var i = 0; i < words.length; i++) {
        var w = words[i], sc = 0;
        if (t.indexOf(w) === 0) sc = 10; else if (t.indexOf(w) >= 0) sc = 6;
        else if (h.indexOf(w) >= 0) sc = 3; else if (s.indexOf(w) >= 0) sc = 2; else if (norm(d.p).indexOf(w) >= 0) sc = 1;
        if (!sc) return;
        score += sc;
      }
      hits.push([score, d]);
    });
    hits.sort(function (a, b) { return b[0] - a[0] || a[1].t.localeCompare(b[1].t); });
    return hits.map(function (x) { return x[1]; });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function item(d) { return '<a href="' + esc(d.u) + '">' + esc(d.t) + (d.s ? "<small>" + esc(d.s) + "</small>" : "") + "</a>"; }
  if (input) {
    input.addEventListener("focus", load, { once: true });
    input.addEventListener("input", function () {
      load().then(function () {
        var r = search(input.value).slice(0, 8);
        box.innerHTML = r.map(item).join("") || (input.value.trim() ? '<a aria-disabled="true">No pages found</a>' : "");
        box.hidden = !box.innerHTML;
        var first = box.querySelector("a"); if (first) first.classList.add("on");
      });
    });
    form.addEventListener("submit", function (e) {
      var first = box.querySelector("a[href]");
      if (first && !box.hidden) { e.preventDefault(); location.href = first.getAttribute("href"); }
    });
    document.addEventListener("click", function (e) { if (!form.contains(e.target)) box.hidden = true; });
  }
  var list = document.getElementById("search-page");
  if (list) {
    var q = new URLSearchParams(location.search).get("q") || "";
    if (input) input.value = q;
    load().then(function () {
      var r = search(q);
      list.innerHTML = r.map(function (d) { return "<li>" + item(d) + "</li>"; }).join("") || "<li>No pages found.</li>";
    });
  }
})();
