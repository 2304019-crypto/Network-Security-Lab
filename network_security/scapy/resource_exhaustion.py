from scapy.all import *

packet_id = 1234

#Fragment-1
frag1 = IP(dst = "192.168.0.104" , id = packet_id, flags = "MF", frag = 0)/Raw(b"A"*8)

#Fragment-2
frag2 = IP(dst = "192.168.0.104" , id=packet_id , flags=0, frag = 7500)/Raw(b"B"*8)

send(frag1, verbose = 0)
send(frag2, verbose = 0)
