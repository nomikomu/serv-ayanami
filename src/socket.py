#!/usr/bin/python

import socket
# socket - basic os concept representing 
# int point of a connection, they are
# biconectional (you can read and write at
# the same time)

# python - client's job:
# * connect; send; receive

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8081))
sock.send('socket hacking')

data = sock.recv(1024)
sock.close()

print('Received: ')
print(data)
