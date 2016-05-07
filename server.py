import socket


host = 'localhost'
port = 1553
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind ((host,port))
s.listen (1)
conn , addr = s.accept()

print ('connexion avec : '+str(addr))
date = None
while True :
    date = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()

while 1 :
    pass
