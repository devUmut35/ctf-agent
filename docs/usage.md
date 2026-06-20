# Kullanım Notları

Bu repo tek başına otomatik solver değil. Daha çok yarışma sırasında hızlıca yön veren bir yardımcı gibi düşün.

## Kurulum

1. `skill/ctf-agent.md` dosyasını aç.
2. İçeriğini kullandığın agent'ın system prompt / custom instructions alanına yapıştır.
3. Yeni sohbette `@ctf` ile challenge detayını yaz.

## Hangi araçlarda kullanılabilir?

System prompt, custom instruction veya benzer bir kalıcı talimat alanı olan çoğu agent ortamında kullanılabilir. Platforma özel bir komut gerektirmez.

## Nasıl daha iyi sonuç verir?

Soruyu ne kadar net verirsen o kadar iyi çalışır.

İyi örnek:

```txt
@ctf elimde Linux x64 binary var. checksec: NX enabled, PIE disabled, Canary yok. gets kullanıyor. Offset 72 buldum.
```

Zayıf örnek:

```txt
@ctf pwn çöz
```

## Dosya verirken

Dosyanın kendisini veremiyorsan en azından şunları koy:

- `file` çıktısı
- `checksec` çıktısı
- hata mesajı
- endpoint / parametre bilgisi
- verilen kaynak kod
- denediğin payload veya komut

## Template kullanımı

`templates/` klasöründeki dosyalar agent için zorunlu değil. Challenge'a göre düzenlenmesi gereken başlangıç dosyaları.

Pwn için:

```bash
python3 templates/pwn_ret2libc.py
python3 templates/pwn_ret2libc.py REMOTE
```

Crypto için:

```bash
python3 templates/crypto_rsa.py
sage templates/crypto_sage.sage
```

Forensics için:

```bash
./templates/forensics_vol.sh dump.mem
```

Author: devUmut35
