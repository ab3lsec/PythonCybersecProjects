import socket
from datetime import datetime
from termcolor import colored

print("-------------------------------")
print("##### PYTHON PORT SCANNER #####")
print("-------------------------------")

target = input("ENTER TARGET IP ADDRESS: ")
startport = int(input("ENTER THE STARTING PORT IN THE RANGE: "))
endport = int(input("ENTER THE LAST PORT IN THE RANGE: "))
print("-------------------------------")

def portscan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"SCANNING THE TARGET {ip}...")
        start_time = datetime.now()
        print("TIME STARTED:", start_time)
        print("-------------------------------")

        open_ports = 0

        for port in range(startport, endport + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))

            if result == 0:
                open_ports += 1
                print(colored(f"PORT {port}: OPEN", 'green'))
            sock.close()

        end_time = datetime.now()
        print("-------------------------------")
        print(f"PORT SCAN COMPLETED IN {end_time - start_time} SECONDS")
        print(f"\nREPORT: {open_ports} OPEN PORTS FOUND ON {target}")

    except socket.gaierror:
        print("HOSTNAME COULD NOT BE RESOLVED!!")

    except socket.error:
        print("COULD NOT CONNECT TO TARGET!!")

    except KeyboardInterrupt:
        sock.close()

portscan(target)
