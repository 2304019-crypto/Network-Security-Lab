import socket
import struct

#Minimum IPv4 header length = 20 bytes
#Minimum TCP header length = 20 bytes
#

s = socket.socket(
	socket.AF_INET,
	socket.SOCK_RAW, 
	socket.IPPROTO_TCP
)

while True:
	packet,address = s.recvfrom(65535)
	
	
	#--------IPv4 Header----------------#
	first_byte = packet[0]
	version = first_byte >> 4
	ihl = first_byte & 0x0F
	
	total_length = struct.unpack("!H", packet[2:4])[0]
	
	ttl = packet[8]
	protocol = packet[9]
	
	source_ip = socket.inet_ntoa(packet[12:16])
	destination_ip = socket.inet_ntoa(packet[16:20])
	
	#---------TCP Header---------------#
	tcp_start = ihl * 4
	tcp_header = packet[tcp_start:]
	
	source_port,destination_port = struct.unpack("!HH", tcp_header[:4])
	
	sequence_number = struct.unpack("!I", tcp_header[4:8])[0]
	ack_number = struct.unpack("!I", tcp_header[8:12])[0]
	
	flags_field = struct.unpack("!H", tcp_header[12:14])[0]
	
	flags = flags_field & 0x1FF
	tcp_header_length = (flags_field >> 12) * 4
	options = tcp_header[20:tcp_header_length]
	
	payload = tcp_header[tcp_header_length:]
	
	print("###################PACKET CAPTURED##############################\n")
	print("-----------TCP INFORMATION---------------\n")
	if flags & 0x01:
		print("FIN")
	if flags & 0x02:
		print("SYN")
	if flags & 0x04:
		print("RST")
	if flags & 0x08:
		print("PSH")
	if flags & 0x10:
		print("ACK")
	if flags & 0x20:
		print("URG")
		
	print("Sequence Number: ", sequence_number)
	print("Acknowledgement number: ", ack_number)
	print("TCP header length:", tcp_header_length)
	print("TCP options:", options.hex())
	print("Payload:", payload.hex())
	
	print("-----------IPv4 INFORMATION--------------- \n")
	print("Version:", version); 
	print("IHL:", ihl)
	print("Header Length:", ihl*4)
	print("Total Length: ", total_length)
	print("TTL:", ttl)
	print("Protocol:", protocol)
	print("Source:", source_ip)
	print("Destination:",destination_ip)
	print("Source port:", source_port)
	print("Destination port:", destination_port)
	print("TCP Header:",tcp_header[:20].hex())
	
