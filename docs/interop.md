# Diğer Skill / Agentlarla Uyum

CTF Agent diğer skill'lerle bağlantılı çalışabilir. Ama rolü her şeyi yapmak değil, CTF bağlamını düzgün kurup ilgili uzmanlığa temiz özet vermektir.

## Görevi

- CTF/lab bağlamını netleştirir.
- Hangi kategori gerektiğini belirler.
- Diğer skill'e aktarılacak kısa handoff üretir.
- Gelen sonucu flag/challenge hedefiyle ilişkilendirir.

## Handoff formatı

```txt
Skill Handoff
- CTF bağlamı: ...
- İstenen uzmanlık: ...
- Verilen veri: ...
- Beklenen çıktı: ...
- Sınır: yalnızca challenge/lab kapsamı
```

## Örnek: Forensics skill'e aktarım

```txt
Skill Handoff
- CTF bağlamı: Forensics challenge
- İstenen uzmanlık: pcap analizi
- Verilen veri: capture.pcap, DNS trafiği şüpheli
- Beklenen çıktı: exfiltration paterni, flag adayları
- Sınır: yalnızca verilen pcap dosyası
```

## Örnek: Code skill'e aktarım

```txt
Skill Handoff
- CTF bağlamı: Crypto challenge
- İstenen uzmanlık: Python script kontrolü
- Verilen veri: RSA çözüm scripti ve n/e/c parametreleri
- Beklenen çıktı: mantık hatası, eksik saldırı ihtimali
- Sınır: challenge verileri
```

## Çakışma önleme

CTF Agent başka skill'in görevini ezmez. Önce context verir, sonra ilgili skill'in uzman çıktısını bekler.

Örnek:

```txt
Bu kısım forensics skill'e uygun. CTF context'i şu: ...
```
