import socket

c= socket.gethostbyname("google.com")
print(c)

d=socket.gethostbyaddr("8.8.8.8")
print(d)