# Context Card Örneği

Bu dosya, CTF Agent'ın başka bir AI/skill'e aktarabileceği kısa bağlam kartı örneğidir.

```txt
CTF Context Card
- Bağlam: CTF / eğitim labı
- Platform/Ortam: picoCTF benzeri web challenge
- Kategori: Web / JWT
- Hedef: Flag'e ulaşmak için auth mantığını analiz etmek
- Verilenler: Login paneli, JWT token, role=user payload
- Sınır: Yalnızca challenge instance'ı
- Sonraki adım: JWT header/payload kontrolü ve zayıf secret testi
```

## Kısa versiyon

```txt
CTF/lab bağlamı var. Kategori web/JWT. Verilen token challenge instance'ından geliyor. Amaç gerçek sistem değil, flag doğrulaması.
```

## Dosyalı örnek

```txt
CTF Context Card
- Bağlam: CTF forensics challenge
- Kategori: PCAP analizi
- Verilenler: capture.pcap
- Hedef: Flag veya exfiltration paterni
- Sınır: Yalnızca verilen pcap dosyası
- Sonraki adım: HTTP, DNS ve FTP trafiğini ayırmak
```
