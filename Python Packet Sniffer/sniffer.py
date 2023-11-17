import socket
from scapy.all import *
from scapy.layers.l2 import Ether

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

interface = "eth0"
s.bind((interface, 0))

try:
	while True:
		rawdata, addr = s.recvfrom(65535)
		packet = Ether(rawdata)
		print(packet.summary())

except KeyboardInterrupt:
	s.close()