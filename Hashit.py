from hashlib import *
def Hashit():
	H_C = str(input('Enter H to hash\nEnter C to crack\n>>> '))
	if H_C == 'H' or H_C == 'h':
		print('\033[32;1m[1]md5[-]\n[2]sha1[×]\n[3]sha224[÷]\n[4]sha256[$]\n[5]sha384[€]\n[6]sha512[¥]\n[7]blake2b[¢]\n[8]blake2s[£]')
		k = int(input('>>> '))
		text = str(input('Enter text to hash : '))
		if k==1:
			print('>>> '+md5(text.encode()).hexdigest())
		elif k==2:
			print('>>> '+sha1(text.encode()).hexdigest())
		elif k==3:
			print('>>> '+sha224(text.encode()).hexdigest())
		elif k==4:
				print('>>> '+sha256(text.encode()).hexdigest())
		elif k==5:
				print('>>> '+sha384(text.encode()).hexdigest())
		elif k==6:
			print('>>> '+sha512(text.encode()).hexdigest())
		elif k==7:
			print('>>> '+blake2b(text.encode()).hexdigest())
		elif k==8:
			print('>>> '+blake2s(text.encode()).hexdigest())
	elif H_C == 'C' or H_C == 'c':
		print('\033[36;1m[1]md5[-]\n[2]sha1[×]\n[3]sha224[÷]\n[4]sha256[$]\n[5]sha384[€]\n[6]sha512[¥]\n[7]blake2b[¢]\n[8]blake2s[£]')
		k = int(input('>>> '))
		ha = str(input('Enter hash to crack : '))
		if k == 1:
			with open('wordlist.txt',mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (md5(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
		elif k == 2:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (sha1(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
		elif k == 3:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (sha224(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break
		elif k == 4:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (sha256(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break
		elif k == 5:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (sha384(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
		elif k == 6:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (sha512(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
		elif k == 7:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (blake2b(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
		elif k == 8:
			with open(file,mode='r')as file:
				for hash in file.readlines():
					hash = hash.strip()
					crack = (blake2s(hash.encode()).hexdigest())
					if crack == ha:
						print('hash crack found ==> '+hash)
						break;
Hashit()