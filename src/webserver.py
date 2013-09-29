#!/usr/bin/python

import socket
import sys

#define Config constants
CFG_SRV_BIND_IF="localhost"
CFG_SRV_BIND_PORT=8080
CFG_SRV_LISTEN_BACKLOG=10
#end of Config constants

# Canned HTTP Response (Apache-like)
HTTP_RESPONSE = """HTTP/1.1 200 OK
Date: Sun, 29 Sep 2013 15:35:05 GMT
Server: Apache/2.2.17 (UNIX) mod_ssl/2.2.17 OpenSSL/0.9.8l DAV/2
Last-Modified: Sat, 28 Sep 2013 01:22:54 GMT
ETag: "20e2b8b-3c-48ee99731f380"
Accept-Ranges: bytes
Content-Length: 49
Connection: close
Content-Type: text/html

<html><body><h1>Herro dza warudo.</h1></body></html>
"""

# Create a TCP/IP socket to listen on 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prevent from "address already in use" upon server restart
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
server_address = (CFG_SRV_BIND_IF, CFG_SRV_BIND_PORT)
print(>>sys.stderr, 'our URL is http://localhost:%d/' % server_address)
print(>>sys.stderr, 'we can only be stopped by CTRL+C')
server.bind(server_address)

# Listen for incomming connections
server.listen(CFG_SRV_LISTEN_BACKLOG)

while True:
	try:
		# Wait for incomming connection
		connection, client_address = server.accept() 
		print(>>sys.stderr, 'New connection from', client_address)

		# Send response
		connection.send("%s" % HTTP_RESPONSE)
		print(>>sys.stderr, 'Response sent.')

		# Indicate that we are going to disconnect
		connection.shutdown(socket.SHUT_WR | socket.SHUT_RD)

		# Closing connection
		connection.close()
		print(>>sys.stderr, 'Connection closed.')
	except:
		# While CTRL+C is pressed etc.
		print("-"*80,'\n * endofprogram * \n'"-"*80)
		break

print(sys.stderr, 'Shutting down...')
server.close()
print(sys.stderr, 'EndMsg: Over.')