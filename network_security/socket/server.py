import socket

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(("127.0.0.1" , 5000))

server.listen()
print("##Server is listening....")

connection,address = server.accept()
print("##Client connected:", address)

while True:
	data = connection.recv(1024)
	
	if not data:
		break
	message = data.decode()
	
	if message == "exit":
		break
	print(message)	
	
	reply =f"Server Recieved: {message}"
	connection.sendall(reply.encode())
 	
connection.close()
server.close()
