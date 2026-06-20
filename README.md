# 🧭 CTF Agent

> Platform bağımsız, system prompt / custom instructions destekleyen AI araçlarında kullanılabilen CTF context ve workflow skill'i.

Yazan: [devUmut35](https://github.com/devUmut35)

---

## Ne İşe Yarar?

CTF Agent, bir yapay zekaya çalışılan işin **CTF / lab / eğitim challenge bağlamında** olduğunu açık, düzenli ve kanıtlanabilir biçimde anlatmak için hazırlanmış bir skill'dir.

Asıl amaç sadece challenge çözmek değildir. Asıl amaç:

- CTF bağlamını net kurmak,
- kullanılan ortamı ve sınırları açıklamak,
- diğer agent/skill'lerin bu bağlamı bozmadan çalışmasına yardımcı olmak,
- gereksiz dosya gezme, uzun retry ve dağınık analizleri azaltmak,
- web, pwn, crypto, reverse, forensics, OSINT ve stego akışlarında hızlı yönlendirme sağlamaktır.

Bu yüzden skill hem **context kurucu** hem de **CTF çalışma akışı yönlendiricisi** gibi davranır.

---

## Kurulum

### Yöntem 1 — System Prompt / Custom Instructions

1. Kullandığın AI aracında system prompt / custom instructions alanını aç
2. `skill/ctf-agent.md` dosyasının içeriğini yapıştır
3. Kaydet
4. Yeni sohbette `@ctf` ile challenge detayını yaz

### Yöntem 2 — Sohbet İçinde

Herhangi bir sohbette şu şekilde kullanabilirsin:

```txt
@ctf [challenge açıklaması / dosya çıktısı / hedef bilgi]
```

---

## Kullanım Mantığı

Tek tetikleyici: `@ctf`

```txt
@ctf picoCTF tarzı web challenge çözüyorum. Login paneli var, cookie base64 gibi duruyor.

@ctf HackTheBox lab ortamındayım. Elimde pcap var, DNS trafiğinde garip subdomainler görünüyor.

@ctf Lokal binary challenge. checksec: NX enabled, PIE disabled, Canary yok. Offset 72 buldum.
```

Skill önce kısa bir **CTF Context Card** çıkarır. Sonra ilgili kategoriye göre yönlendirir.

---

## Python Gerekli mi?

Hayır. Skill'i kullanmak için Python gerekmez.

Asıl dosya:

```txt
skill/ctf-agent.md
```

`templates/` klasöründeki Python dosyaları zorunlu değildir. Bunlar sadece CTF çözerken kullanılabilecek başlangıç scriptleridir. Scriptleri çalıştırmak istersen Python ve `requirements.txt` gerekir.

---

## Repo Yapısı

```txt
ctf-agent/
├── README.md
├── LICENSE
├── SECURITY.md
├── CHANGELOG.md
├── REPO_INFO.md
├── skill/
│   └── ctf-agent.md          ← Ana skill dosyası
├── docs/
│   ├── usage.md              ← Kullanım notları
│   ├── scope.md              ← Kapsam ve sınırlar
│   └── interop.md            ← Diğer skill/agentlarla çalışma notları
├── examples/
│   ├── context-card.md       ← CTF bağlam kartı örneği
│   ├── web-example.md
│   ├── crypto-example.md
│   └── forensics-example.md
└── templates/
    ├── pwn_ret2libc.py
    ├── pwn_rop_chain.py
    ├── crypto_rsa.py
    ├── crypto_sage.sage
    ├── web_jwt_crack.py
    └── forensics_vol.sh
```

---

## Kapsanan Kategoriler

| Kategori | İçerik |
|---|---|
| 🔴 **PWN** | Stack overflow, format string, ROP, ret2libc, basic heap |
| 🟠 **Web** | SQLi, XSS, SSRF, SSTI, JWT, IDOR, upload, traversal |
| 🟡 **Crypto** | RSA, AES-CBC, XOR, padding oracle, hash, Wiener |
| 🟢 **Reverse** | Ghidra, strings, anti-debug, patching, basic VM reversing |
| 🔵 **Forensics** | Volatility, Wireshark, disk/memory/log analizi |
| 🟣 **OSINT** | Metadata, geolocation, username, dorking |
| 🩶 **Stego** | LSB, binwalk, steghide, zsteg, spektrogram |
| ⚫ **Misc** | Jail, scripting, blockchain, esolang |

---

## Hız Notu

CTF Agent uzun uzun dosya gezmez. Kullanıcı dosya vermediyse dosya aramaz. Aynı bağlantı/DNS hatasını sürekli tekrar etmez. Önce net teşhis verir, sonra kullanıcı isterse derin analize geçer.

---

## Kullanım Notu

Bu repo CTF yarışmaları, eğitim labları ve izinli güvenlik çalışmaları için hazırlandı. Gerçek sistemlerde izinsiz kullanım amacıyla hazırlanmadı.

---

## Lisans

MIT — Copyright (c) 2026 Umutcan Altan (devUmut35).

---

*CTF yarışmaları, eğitim platformları ve izinli lab ortamları için tasarlanmıştır. Author: devUmut35*
