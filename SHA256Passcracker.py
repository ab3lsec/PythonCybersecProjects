from pwn import *
import sys
from termcolor import colored

print("--------------------------------------")
print("##### PYTHON SHA256 HASH CRACKER #####")
print("--------------------------------------")

if len(sys.argv) != 2:
    print("REQUIRES sha256 HASH!!")
    print(f"CORRECT SYNTAX: {sys.argv[0]} <sha256sum> ")
    exit()

userhash = sys.argv[1]
passlist = "/usr/share/wordlists/rockyou.txt" 
attempts = 0

with log.progress(f"ATTEMPTING TO CRACK: {userhash}!\n") as p:
	with open(passlist, "r", encoding='latin-1') as passfile:
		for password in passfile:
			password = password.strip("\n").encode('latin-1')
			passwordhash = sha256sumhex(password)
			p.status(f"{[attempts]} {password.decode('latin-1')} == {passwordhash}")
			
            if passwordhash == userhash:
				p.success(f"PASSWORD FOUND AFTER {attempts} ATTEMPTS!! VALID PASSWORD: {colored(password.decode('latin-1'), 'green')}")
				exit()

			attempts += 1
            
		p.failure("PASSWORD NOT FOUND!!")
