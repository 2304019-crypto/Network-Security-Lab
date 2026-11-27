from scapy.all import IP, Raw

packet_id = 33333

# Fragment 1
frag1 = IP(
    dst="192.168.10.20",
    id=packet_id,
    flags="MF",
    frag=0
) / Raw(b"A" * 1000)

# Fragment 2 overlaps part of fragment 1
frag2 = IP(
    dst="192.168.10.20",
    id=packet_id,
    flags=0,
    frag=50
) / Raw(b"B" * 1000)

frag1.show()
frag2.show()
