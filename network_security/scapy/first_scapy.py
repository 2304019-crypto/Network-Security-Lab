from scapy.all import *

target = "192.168.0.105"

packet = IP(dst = target) / TCP(dport = 8000 , flags="S")

print("Sending TCP SYN......")

response = sr1(packet , timeout = 4, verbose = 0)

if response is None:
	print("No response received")
elif response.haslayer(TCP):
	print("Response received!")
	print("Source IP:",response[IP].src)
	print("Destination IP:",response[IP].dst)
	print("TCP flags:",response[TCP].flags)
	print("Source port:",response[TCP].sport)
	print("Destination port:",response[TCP].dport)
else:
	print("Reveived a non TCP response!")
