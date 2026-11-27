import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

while True:
	message = input()
	
	client.sendall(message.encode())
	
	if message == "exit":
		break
		
	response = client.recv(1024)
	
	print("##Server:",response.decode())

client.close()
