#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time

import simulation_parameters as sp
import process
import cpu
import memory
import swapping

# Global variables
KB = 1024
start_time = None
swapping_obj = None
memory_obj = None

# Object to store all the OS simulation parameters
sim_param = sp.SimulationParameters()

# CPU initialization with its ready queue.
cpu_obj = cpu.CPU()

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


def initialize():
	# Swapping initialization
	global swapping_obj 
	swapping_obj = swapping.Swapping(sim_param.swap_memory, sim_param.page_size * KB)

	# Memory initialization
	global memory_obj 
	memory_obj = memory.Memory(sim_param.real_memory, sim_param.page_size, swapping_obj)

# Assigns the RealMemory parameter to the object with the Simulation parameters.
def real_mem_param(*p):
	params = p[0]
	sim_param.real_memory = int(params[0])
	print(sim_param.real_memory)
	connection.send("parametros:" + ', '.join(params))

# Assigns the SwapMemory parameter to the object with the Simulation parameters.
def swap_mem_param(*p):
	params = p[0]
	sim_param.swap_memory = int(params[0])
	print(sim_param.swap_memory)
	connection.send("parametros:" + ', '.join(params))

# Assigns the PageSize parameter to the object with the Simulation parameters.
def page_size_param(*p):
	params = p[0]
	sim_param.page_size = int(params[0])
	print(sim_param.page_size)
	connection.send("parametros:" + ', '.join(params))
	initialize()

def create(*p):
	connection.send("Scheduling: PrioExp, intente CreateP")
	return "funcion create"

def address(*p):
	params = p[0]
	pid = int(params[0])
	v = int(params[1])
	process = cpu_obj.current_process
	pr_id = process.pid
	page_num = 0
	if int(pr_id) != int(pid):
		msg = "{:0.2f} {} no se está ejecutando. Se ignora.".format(time.time(), pid)
	#verificar tamaño de proceso
	else:
		page_num = memory_obj.getProcessPage(pid)
		if not page_num:
			print("load process")
			page_num = memory_obj.loadProcess(pid)
		print(page_num)
		real_address = int(page_num) * KB + v

		msg = "{:0.2f} real address: {}".format(time.time(),real_address)
	
	connection.send(msg)
	return "funcion address"

def create_priority(*p):

	global start_time
	global cpu_obj

	params = p[0]
	size = int(params[0])
	priority = int(params[1])
	print(params)
	# Process to insert
	my_p = None
	if start_time is None:
		my_p = process.Process(size, priority, 0.00, sim_param.page_size * KB)
		start_time = time.time()
	else:
		my_p = process.Process(size, priority, time.time() - start_time, int(sim_param.page_size) * KB)

	cpu_obj.addProcess(my_p)
	memory_obj.loadProcess(my_p.pid)

	msg = "{:0.2f} process {} created size {} pages".format(my_p.time_created, my_p.pid, my_p.num_of_pages)
	connection.send(msg)

	return "funcion createp"

# Assigns the Quantum parameter to the object with the Simulation parameters.
def quantum(*p):
	connection.send("Scheduling: PrioExp, no hay quantum")
	return "funcion quantum"

def termina_proceso(*p):
	params = p[0]
	pid = params[0]
	msg = "{:0.2f} Proceso {} terminado.".format(my_p.time_created, pid)
	connection.send(msg)
	
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
		data = msg

		if "//" in msg:
			msgSplit = msg.split("//")
			data = msgSplit[0]

		command = data.split()

		comando = {
			'RealMemory': real_mem_param,
			'SwapMemory': swap_mem_param,
			'PageSize': page_size_param,
			'Create': create,
			'Address': address,
			'CreateP': create_priority,
			'Quantum': quantum,
			'Fin': termina_proceso,
			'End': end_simulation
		}.get(command[0], invalid)(command[1:])

		if command:
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

