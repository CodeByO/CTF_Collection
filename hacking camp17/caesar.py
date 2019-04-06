# _*_ coding: cp949 _*_

def encrypt(passwd):
	result = ""
	for i in passwd:
		result += chr(ord(i) + shift)
	return result

def decrypt(passwd):
	result = ""
	for i in passwd:
		result += chr(ord(i) - shift)
	return result

shift = int(input("INPUT THE SHIFT(NUM) : "))
passwd = input("INPUT THE PASSWORD : ")

result1 = encrypt(passwd)
result2 = decrypt(result1)

print("========= RESULT =========")
print("ENCRYPTED : ", result1)
print("DECRYPTED : ", result2)
print("==========================")