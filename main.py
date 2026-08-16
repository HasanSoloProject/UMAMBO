#!/usr/bin/env python3
"""UMAMBO — Premium OTP Spammer."""
import os, sys, time, json, socket
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import spam, prank_call
from junk import G, C, Y, R, P, W, N

HIDDEN = True
WORKDIR = os.path.expanduser("~/umambo")
C_FILE = os.path.join(WORKDIR, "cnt.json")
os.makedirs(WORKDIR, exist_ok=True)

def ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)); i = s.getsockname()[0]; s.close(); return i
    except: return "127.0.0.1"

def cnt():
    try:
        d = {"c": 0, "l": ""}
        if os.path.exists(C_FILE): d = json.load(open(C_FILE))
        d["c"] += 1; d["l"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        json.dump(d, open(C_FILE, "w"))
        return d["c"]
    except: return "?"

def lobby():
    global HIDDEN
    os.system("clear")
    print(f"{R}")
    print("██╗░░░██╗███╗░░░███╗░█████╗░███╗░░░███╗██████╗░░█████╗░")
    print("██║░░░██║████╗░████║██╔══██╗████╗░████║██╔══██╗██╔══██╗")
    print("██║░░░██║██╔████╔██║███████║██╔████╔██║██████╦╝██║░░██║")
    print("██║░░░██║██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██║░░██║")
    print("╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚═╝░██║██████╦╝╚█████╔╝")
    print("░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░")
    print(f"{N}")
    i = ip(); u = cnt()
    print(f"  {W}Author : {C}Mimbu{N}")
    print(f"  {W}User   : {Y}Premium{N}")
    if HIDDEN: print(f"  {R}IP     : ××××××××{N}")
    else: print(f"  {R}IP     : {i}{N}")
    print(f"  {W}User   : {P}× {u}{N}")
    print("")
    print(f"  {Y}[!] Saran: jeda 1 jam tiap spam biar ga keblokir server.{N}")
    print("")
    print(f"  {P}[ 1 ]{N} {W}Spam OTP WhatsApp/SMS{N}")
    print(f"  {P}[ 2 ]{N} {W}Prank Call{N}")
    print(f"  {P}[ 3 ]{N} {W}Spam Email (dalam pengerjaan){N}")
    print(f"  {P}[ 4 ]{N} {W}Spam NGL (dalam pengerjaan){N}")
    print(f"  {P}[ 5 ]{N} {W}Hubungi Admin{N}")
    print(f"  {P}[ 6 ]{N} {W}Perlihatkan IP Saya{N}")
    print(f"  {P}[ 7 ]{N} {W}Spam Pairing Code (dalam pengerjaan){N}")
    print(f"  {P}[ 8 ]{N} {W}Exit{N}")
    print("")
    c = input(f"  {C}[?] Pilih : {N}").strip()
    if c == "1":
        p = input(f"\n  {C}[?] Nomor target : {N}⟩⟩⟩ ").strip()
        if p:
            p = "".join(x for x in p if x.isdigit() or x == "+")
            if p.startswith("0"): p = "+62" + p[1:]
            elif p.startswith("62") and not p.startswith("+"): p = "+" + p
            elif not p.startswith("+"): p = "+" + p
            spam(p)
    elif c == "2":
        p = input(f"\n  {C}[?] Nomor target : {N}⟩⟩⟩ ").strip()
        if p:
            p = "".join(x for x in p if x.isdigit() or x == "+")
            if p.startswith("0"): p = "+62" + p[1:]
            elif p.startswith("62") and not p.startswith("+"): p = "+" + p
            elif not p.startswith("+"): p = "+" + p
            prank_call(p)
    elif c == "3":
        print(f"\n  {Y}[!] Spam Email masih dalam pengerjaan.{N}")
        time.sleep(2)
        lobby()
    elif c == "4":
        print(f"\n  {Y}[!] Spam NGL masih dalam pengerjaan.{N}")
        time.sleep(2)
        lobby()
    elif c == "5":
        print(f"\n  {G}[*] Mengarahkan ke WhatsApp Admin...{N}")
        time.sleep(1)
        os.system("termux-open-url https://wa.me//6288293898844")
    elif c == "6":
        HIDDEN = False
        print(f"\n  {R}[!] IP Anda : {ip()}{N}")
        input(f"\n  {W}[Enter] Kembali...{N}")
        HIDDEN = True
        lobby()
    elif c == "7":
        print(f"\n  {Y}[!] Bentar napa, susah oi bikinnya.{N}")
        time.sleep(2)
        lobby()
    elif c == "8":
        print(f"\n  {R}[!] Exit.{N}")
        sys.exit(0)
    else:
        lobby()

if __name__ == "__main__":
    while True: lobby()
