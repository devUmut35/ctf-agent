#  CTF Agent — AI Destekli CTF Skill'i

> Platform bağımsız, system prompt destekleyen agentlarda kullanılabilen CTF yardımcı skill'i.

Yazan: [devUmut35](https://github.com/devUmut35)

---

## Ne İşe Yarar?

CTF yarışmalarında anlık teknik destek almak için tasarlandı. Binary pwn'dan kripto'ya, web'den forensics'e kadar birçok kategoride hızlı analiz akışı, araç komutları ve başlangıç şablonları sunar.

Amaç otomatik çözüm vadetmek değil; challenge sırasında daha düzenli düşünmek, doğru araçları hatırlamak ve denemeleri hızlandırmak.

---

## Kurulum

### Yöntem 1 — System Prompt / Custom Instructions

1. Kullandığın agent ya da AI aracında system prompt / custom instructions alanını aç
2. `skill/ctf-agent.md` dosyasının içeriğini yapıştır
3. Kaydet
4. Yeni sohbette `@ctf` ile challenge detayını yaz

### Yöntem 2 — Sohbet İçinde

Herhangi bir sohbette şu şekilde kullanabilirsin:

```txt
@ctf [sorun veya challenge içeriği]
```

---

## Kullanım

Tek tetikleyici: `@ctf`

```txt
@ctf bu binary'de ne var? [challenge dosyasını / çıktıları ekle]

@ctf AES-CBC şifrelemesi veriliyor, IV biliniyor, ne kontrol edeyim?

@ctf pcap dosyasını analiz etmem gerekiyor, nereden başlayayım?

@ctf JWT token var, alg:none ve zayıf secret kontrol edeceğim
```

Menü yok. Komut ezberi yok. Challenge detayını ver, akışı beraber ilerlet.

---

## Python Gerekli mi?

Hayır. Agent skill'ini kullanmak için Python gerekmez.

Asıl dosya:

```txt
skill/ctf-agent.md
```

`templates/` klasöründeki Python dosyaları zorunlu değildir. Bunlar sadece CTF çözerken kullanabileceğin hazır başlangıç scriptleridir. Scriptleri çalıştırmak istersen Python ve `requirements.txt` gerekir.

---

## Repo Yapısı

```txt
ctf-agent/
├── README.md              ← Bu dosya
├── skill/
│   └── ctf-agent.md       ← Ana skill dosyası
├── docs/
│   ├── usage.md           ← Kullanım notları
│   └── scope.md           ← Kullanım kapsamı
├── examples/
│   ├── web-example.md
│   ├── crypto-example.md
│   └── forensics-example.md
└── templates/
    ├── pwn_ret2libc.py    ← Pwntools ret2libc şablonu
    ├── pwn_rop_chain.py   ← ROP zinciri şablonu
    ├── crypto_rsa.py      ← RSA saldırı şablonu
    ├── crypto_sage.sage   ← SageMath Wiener şablonu
    ├── web_jwt_crack.py   ← JWT brute-force şablonu
    └── forensics_vol.sh   ← Volatility3 hızlı komutlar
```

---

## Kapsanan Kategoriler

| Kategori | İçerik |
|---|---|
| 🔴 **PWN** | Stack overflow, heap, format string, ROP, SROP, ret2libc, UAF |
| 🟠 **Web** | SQLi, XSS, SSRF, SSTI, JWT, Deserialization, HTTP Smuggling |
| 🟡 **Kripto** | RSA, AES-CBC, Padding Oracle, XOR, Hash Extension, Wiener |
| 🟢 **Rev** | Ghidra, anti-debug bypass, VM reversing, obfuscation |
| 🔵 **Forensics** | Volatility, Wireshark, disk/memory analizi, log forensics |
| 🟣 **OSINT** | Geolocation, metadata, username enum, Google dorking |
| 🩶 **Stego** | LSB, spektrogram, binwalk, steghide, zsteg |
| ⚫ **Misc** | Jail escape, blockchain, scripting, esolangs |

---

## Şablonlar

`templates/` klasöründeki dosyalar tam çözüm değildir. Challenge'a göre düzenlenecek başlangıç noktalarıdır.

---

## Kullanım Notu

Bu repo CTF yarışmaları, eğitim labları ve izinli güvenlik çalışmaları için hazırlandı. Gerçek sistemlerde izinsiz kullanım amacıyla hazırlanmadı.

---

## Lisans

MIT — Copyright (c) 2026 Umutcan Altan (devUmut35).

---

*CTF yarışmaları ve etik hacking platformları için tasarlanmıştır. Author: devUmut35*
