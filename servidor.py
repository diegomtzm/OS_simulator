#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

# accept() returns an open connection between the server and client, along with the address of the client.
# The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().

def create(*p):
	params = p[0]
	print (params)
	connection.send("parametros: " + ', '.join(params))
	return "funcion create"

def address(*p):
	params = p[0]
	print (params)
	connection.send("parametros: " + ', '.join(params))
	return "funcion address"

def create_priority(*p):
	params = p[0]
	print (params)
	connection.send("parametros: " + ', '.join(params))
	return "funcion createp"

def quantum(*p):
	params = p[0]
	print (params)
	connection.send("parametros: " + ', '.join(params))
	return "funcion quantum"

def termina_proceso(*p):
	params = p[0]
	print (params)
	connection.send("parametros: " + ', '.join(params))
	return "funcion fin"

def end_simulation(*p):
	print ("[end]")
	connection.send("simulacion terminada")
	return "funcion end"

def invalid(*p):
	print ("Comando invalido")
	connection.send("comando invalido")
	return "funcion invalid"


try:
	print >>sys.stderr, 'connection from', client_address

    # Receive the data 
	while True:   
		msg = connection.recv(256)
		data = msg.split()

		comando = {
			'Create': create,
			'Address': address,
			'CreateP': create_priority,
			'Quantum': quantum,
			'Fin': termina_proceso,
			'End': end_simulation,
		}.get(data[0], invalid)(data[1:])

		if data:
			print >>sys.stderr, 'server received "%s"' % comando
		else:
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()

finally:
     # Clean up the connection
	print >>sys.stderr, 'se fue al finally'
	connection.close()

# When communication with a client is finished, the connection needs to be cleaned up using close(). 
# This example uses a try:finally block to ensure that close() is always called, even in the event of an error.

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

