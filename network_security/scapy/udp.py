from scapy.all import *

packet = IP(dst="127.0.0.1") / UDP(dport=9999) / Raw(load="Hello")

packet.show()
