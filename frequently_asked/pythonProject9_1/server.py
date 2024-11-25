import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',12345))

s.listen(3)
while True:
    c,address = s.accept()
    c.send('Hi.. am Linda'.encode())
    print(c.recv(1024).decode())
    c.close()
    break

