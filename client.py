import socket


host = 'localhost'
port = 1553
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn =s.connect ((host,port))
s.send('hello world !!!!')
data = s.recv(1024)
s.close()
print 'recived' , repr(data)

while 1:
    pass
