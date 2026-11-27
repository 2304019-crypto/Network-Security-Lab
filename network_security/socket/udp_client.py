import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	message = input("Enter Message >> ")
	client.sendto(message.encode(),('127.0.0.1', 5000))
	if message == "exit":
		break
	data,address = client.recvfrom(1024)
	print("Server Replied >>", data.decode())

client.close()
