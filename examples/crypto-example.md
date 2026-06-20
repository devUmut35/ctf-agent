# Crypto örnek kullanım

## Challenge

RSA veriliyor: `n`, `e`, `c` var. Padding hakkında bilgi yok.

## Sorulacak örnek

```txt
@ctf RSA'da n e c verilmiş, e=3. Nasıl kontrol edeyim?
```

## İlk bakılacaklar

- `n` kaç bit?
- `e` küçük mü?
- Aynı mesaj birden fazla modulus ile verilmiş mi?
- `n` factordb gibi yerde parçalanıyor mu?
- Padding yoksa direkt kök alma tutuyor mu?

## Komut / script

```bash
python3 templates/crypto_rsa.py
sage templates/crypto_sage.sage
```

Ben genelde önce küçük `e` ve faktorizasyon ihtimaline bakıyorum. Sonra Wiener/common modulus gibi yollara geçiyorum.
