from scapy.all import *

def analyze(packet):

    if packet.haslayer(IP) and packet.haslayer(ICMP):

        ip = packet[IP]
        icmp = packet[ICMP]

        print("==============================")
        print("Source      :", ip.src)
        print("Destination :", ip.dst)
        print("Type        :", icmp.type)
        print("Code        :", icmp.code)

        if icmp.type == 8:
            print("Message     : Echo Request")

        elif icmp.type == 0:
            print("Message     : Echo Reply")

        elif icmp.type == 3:
            print("Message     : Destination Unreachable")

        elif icmp.type == 11:
            print("Message     : Time Exceeded")

        else:
            print("Message     : Other ICMP message")

sniff(
    filter="icmp",
    prn=analyze,
    store=False
)
