import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost',12345))
c.send("Hi, am the client".encode())
print(c.recv(1024).decode())
