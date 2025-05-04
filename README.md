# Project Description

This project uses `mitmproxy` to intercept and dump the contents of all JavaScript files loaded by a browser when visiting a website. 
Currently has two working versions, a manual one that requires the user to force a fresh search in their browser (via ctrl+shift+R for example) and an experimental automatic one that takes any sort of page request and uses cache-busting to force a full redownload (WIP).

---

## Iterative process

I approached this project with an iterative process in mind, adding complexity between versions. All versions are available with no version control since this is not a production project.
**Iterarions:**
1. curl version
2. cache issues
3. understanding flow request vs flow response
4. forcing no cache
   1. fmodifying the request/response headers
   2. using cache busting on the .js declarations

---

## Relevant resources
[Official mitmproxy http doc](https://docs.mitmproxy.org/stable/api/mitmproxy/http.html)
[Save resource files from visited websites](https://forums.gentoo.org/viewtopic-p-8817597.html?sid=b43ce5d86e9b152de33581dccb53263f)
[Save body response from URL](https://stackoverflow.com/questions/48119483/save-body-response-from-specific-url-to-file-and-decode-it-using-mitmproxy)
[Injecting js in HTML content](https://pankajmalhotra.com/Injecting-Javascript-In-HTML-Content-Using-MITM-Proxy)
[How to remove headers mitmproxy](https://github.com/mitmproxy/mitmproxy/issues/3968)
[How (and how not) to control caches](https://www.mnot.net/cache_docs/#CONTROL)
[What is cache busting](https://www.curtiscode.dev/post/what-is-cache-busting)
[Clear-Site-Data header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Clear-Site-Data)
[What is the correct way to do cache busting](https://forum.level1techs.com/t/cache-busting-whats-the-correct-way/183217/7)

---

## Usage Guide

### 1. Dependancies

- `Python` 3.12
- `mitmproxy` 12.0.0 (installed via pipx)
- some web proxy (optional, currently using `Proxy Switcher` addon for Chrome based browsers)

### 2. Setup

Clone the repo and use via makefile commands:

```bash
git clone https://your.gitlab.repo/k8s-infra.git
cd k8s-infra
make stable
```

---

## Author
Francisco Bolzan - updated 03/05/2025