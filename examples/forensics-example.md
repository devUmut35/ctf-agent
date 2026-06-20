# Forensics örnek kullanım

## Challenge

Bir memory dump veya pcap geliyor. Direkt flag aramak bazen yetiyor ama genelde önce sistemli gitmek daha iyi.

## Memory dump için

```txt
@ctf elimde memory dump var, şüpheli process ve flag aramam lazım
```

```bash
file dump.mem
strings dump.mem | grep -i "flag\|password\|secret"
./templates/forensics_vol.sh dump.mem
```

## Pcap için

```bash
tshark -r capture.pcap -Y "http"
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | sort | uniq -c
tshark -r capture.pcap --export-objects http,./output/
```

Benim alışkanlık: önce strings, sonra protokol/proses ayrımı, sonra dosya çıkarma.
