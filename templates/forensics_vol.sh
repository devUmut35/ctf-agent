#!/usr/bin/env bash
# Volatility3 hızlı komut listesi
# Kullanım: ./forensics_vol.sh dump.mem

set -e

MEM="$1"

if [ -z "$MEM" ]; then
  echo "Kullanım: $0 dump.mem"
  exit 1
fi

echo "[*] Sistem bilgisi"
vol -f "$MEM" windows.info || true

echo "[*] Process listesi"
vol -f "$MEM" windows.pslist || true

echo "[*] Process tree"
vol -f "$MEM" windows.pstree || true

echo "[*] Komut satırları"
vol -f "$MEM" windows.cmdline || true

echo "[*] Ağ bağlantıları"
vol -f "$MEM" windows.netscan || true

echo "[*] Dosya arama - flag keyword"
vol -f "$MEM" windows.filescan | grep -i "flag\|secret\|password" || true
