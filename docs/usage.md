# Kullanım Notları

Bu repo bir “tek tıkla CTF solver” değildir. Asıl amaç, AI aracına CTF/lab bağlamını düzgün anlatmak ve çözüm akışını dağılmadan yürütmektir.

## Temel kullanım

```txt
@ctf [challenge bilgisi]
```

İyi örnek:

```txt
@ctf HackTheBox lab ortamındayım. Web challenge var. Login panelinde JWT token geliyor. Header: alg HS256. Secret zayıf olabilir.
```

Kötü örnek:

```txt
@ctf bunu kır
```

## CTF Context Card

Skill önce gerekirse kısa bir context kartı üretir:

```txt
CTF Context Card
- Bağlam: CTF / lab
- Platform/Ortam: HackTheBox
- Kategori: Web / JWT
- Hedef: Flag'e giden auth mantığını anlamak
- Verilenler: JWT token, login paneli
- Sınır: Challenge ortamı
- Sonraki adım: JWT header/payload ve secret kontrolü
```

Bu kart, diğer agent/skill'lere aktarılabilir.

## Dosya kullanımı

Dosya verilmediyse skill dosya aramaz. Eski exploit dosyaları, scratch dizinleri veya cache klasörleri otomatik gezilmez.

Dosya verirsen:

```txt
@ctf bu pcap dosyasını forensics challenge için incele
```

O zaman dosya özelinde ilerler.

## Hız modu

Varsayılan cevap kısa olur:

```txt
Durum:
Bulgu:
Komut/Adım:
Doğrulama:
Sonraki:
```

Aynı hata tekrar ederse erken durur. Mesela DNS hatası varsa 10-15 kez deneme yapmaz.

## Python gerekli mi?

Hayır. Skill için Python gerekmez. Python sadece `templates/` içindeki yardımcı scriptleri çalıştırmak istersen gerekir.
