import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4 , SOCK_STREAM = TCP
print("Socket Created Successfully")

s.close()
