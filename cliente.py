#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.

import socket
import sys
import endP as finalP

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.

while True:
    mensaje = raw_input("Mensaje a enviar al servidor: ")
    
    if mensaje == "End":
        break
    
    sock.sendall(mensaje)

    respuesta = sock.recv(256)
    
    print >>sys.stderr, 'cliente received "%s"' % respuesta


print >>sys.stderr, 'closing socket'
finalP
sock.close()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

