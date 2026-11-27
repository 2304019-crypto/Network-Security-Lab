import socket

server = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 5000))

print("##UDP Server Listening.....")

while True:

	data,address = server.recvfrom(1024)
	print("##Client Address:", address)
	message = data.decode()
	if not message:
		break
	print("Client >> ", message)
	if message == "exit":
		break
	reply = f"Server recieved: {message}"
	server.sendto(reply.encode(),address)
	
server.close()
