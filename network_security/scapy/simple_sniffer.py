from scapy.all import *

def analyze_tcp(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        ip = packet[IP]
        tcp = packet[TCP]

        print(
            f"{ip.src}:{tcp.sport} "
            f"-> "
            f"{ip.dst}:{tcp.dport} "
            f"Flags={tcp.flags}"
        )

sniff(
    filter="tcp",
    prn=analyze_tcp,
    store=False
    ) 
  #store = false => doesn't store packets in memory
