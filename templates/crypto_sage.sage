# SageMath RSA not şablonu
# Çalıştırma: sage crypto_sage.sage

from Crypto.Util.number import long_to_bytes

n = Integer(0)
e = Integer(65537)
c = Integer(0)


def wiener_attack(e, n):
    # d çok küçükse denenir. Her soruda çalışmaz.
    cf = continued_fraction(Integer(e) / Integer(n))
    for conv in cf.convergents():
        k = conv.numerator()
        d = conv.denominator()
        if k == 0:
            continue
        phi_candidate = (e * d - 1) // k
        s = n - phi_candidate + 1
        discr = s * s - 4 * n
        if discr >= 0 and Integer(discr).is_square():
            return Integer(d)
    return None


d = wiener_attack(e, n)
if d:
    print("[+] d bulundu:", d)
    m = power_mod(c, d, n)
    print(long_to_bytes(int(m)))
else:
    print("[-] Wiener tutmadı")
