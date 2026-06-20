#!/usr/bin/env python3
# RSA challenge notları için küçük helper.
# n, e, c değerlerini challenge'dan alıp doldur.

from Crypto.Util.number import long_to_bytes, inverse
import math

n = 0
e = 65537
c = 0


def try_small_e():
    """e küçükse ve padding yoksa bazen direkt kök alınır."""
    try:
        import gmpy2
    except ImportError:
        print("gmpy2 yok: pip install gmpy2")
        return

    m, exact = gmpy2.iroot(c, e)
    if exact:
        print("[+] small-e tuttu:", long_to_bytes(int(m)))
    else:
        print("[-] small-e direkt tutmadı")


def decrypt_with_pq(p, q):
    """p ve q bulunduysa normal RSA çözme."""
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))


def quick_checks():
    print("n bit length:", n.bit_length())
    print("gcd(e, n):", math.gcd(e, n))
    if e in (3, 5, 17):
        print("[*] e küçük, small-e / broadcast ihtimali bakılabilir")


if __name__ == "__main__":
    quick_checks()
    # try_small_e()
    # decrypt_with_pq(p, q)
