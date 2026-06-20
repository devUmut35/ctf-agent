#!/usr/bin/env python3
# JWT HS256 wordlist deneme şablonu.
# CTF'de verilen token için lokal brute-force yapar.

import sys
import jwt


def usage():
    print(f"Kullanım: {sys.argv[0]} <token> <wordlist>")
    raise SystemExit(1)


if len(sys.argv) != 3:
    usage()

token = sys.argv[1].strip()
wordlist = sys.argv[2]

with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        secret = line.strip()
        if not secret:
            continue
        try:
            data = jwt.decode(token, secret, algorithms=["HS256"])
            print("[+] secret bulundu:", secret)
            print("[+] payload:", data)
            break
        except jwt.InvalidTokenError:
            pass
    else:
        print("[-] wordlist içinde bulunamadı")
