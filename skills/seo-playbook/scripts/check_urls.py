#!/usr/bin/env python3
"""Cek status HTTP, redirect, dan tanda noindex dari daftar URL.

Pemakaian:
    python scripts/check_urls.py urls.txt

urls.txt berisi satu URL per baris. Hanya membaca (GET), tidak mengubah apa pun.
Hanya pakai pada situs milikmu atau yang kamu punya izin untuk dicek.
"""
import re
import sys
import time
import urllib.request
import urllib.error

UA = "Mozilla/5.0 (compatible; seo-roadmap-checker/1.0)"
META_ROBOTS = re.compile(r'<meta[^>]+name=["\']robots["\'][^>]*>', re.I)


def check(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(300_000).decode("utf-8", errors="ignore")
            header_robots = r.headers.get("X-Robots-Tag", "")
            meta = META_ROBOTS.search(body)
            meta_txt = meta.group(0) if meta else ""
            noindex = "noindex" in header_robots.lower() or "noindex" in meta_txt.lower()
            return {"url": url, "status": r.status, "final_url": r.geturl(),
                    "redirected": r.geturl().rstrip("/") != url.rstrip("/"), "noindex": noindex}
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "final_url": url, "redirected": False, "noindex": False}
    except Exception as e:  # noqa: BLE001
        return {"url": url, "status": f"ERR {type(e).__name__}", "final_url": url, "redirected": False, "noindex": False}


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    with open(sys.argv[1], encoding="utf-8") as f:
        urls = [u.strip() for u in f if u.strip() and not u.startswith("#")]
    print("status\tnoindex\tredirect\turl\tfinal_url")
    for u in urls:
        r = check(u)
        print(f"{r['status']}\t{r['noindex']}\t{r['redirected']}\t{r['url']}\t{r['final_url']}")
        time.sleep(1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
