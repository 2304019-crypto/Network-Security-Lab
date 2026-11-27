from scapy.all import *

def analyze_packet(packet):
	print("\n=====================================")
	#layer-2 Ethernet
	if packet.haslayer(Ether):
		ether = packet[Ether]
		print("[Ethernet]")
		print("Source MAC:",ether.src)
		print("Dest MAC:",ether.dst)
	#layer-3 IP
	if packet.haslayer(IP):
		ip=packet[IP]
		print("\n[IP]")
		print("Source IP:",ip.src)
		print("Dest IP:",ip.dst)
		print("TTL:",ip.ttl)
	#layer-4 TCP
	if packet.haslayer(TCP):
		tcp=packet[TCP]
		print("\n[TCP]")
		print("Source Port:",tcp.sport)
		print("Dest Port:",tcp.dport)
		print("Flags:",tcp.flags)
	elif packet.haslayer(UDP):
		udp=packet[UDP]
		print("\n[UDP]")
		print("Source port:",udp.sport)
		print("Dest port:",udp.dport)
	#Raw Payload
	if packet.haslayer(Raw):
		data=packet[Raw].load
		print("\n[RAW PAYLOAD]")
		print("Length:",len(data))
		print("Bytes:",repr(data))
		
sniff(iface='enp0s3', filter = "ip", prn=analyze_packet, store=False)
