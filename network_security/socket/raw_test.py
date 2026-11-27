import socket

s = socket.socket(
    socket.AF_INET,
    socket.SOCK_RAW,
    socket.IPPROTO_TCP
)

print("Raw socket created!")

while True:
    packet, address = s.recvfrom(65535)

    print("Packet received!")
    print("Length:", len(packet))
    print("First 20 bytes:")
    print(packet[:20])
