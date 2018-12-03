from texttable import Texttable as tt
import process as p
import ready_queue as rq #queue
import cpu

class endP: 

 def __init__(self):
 	self.final = [0, 0, 0, 0, 0, 0, 0, 0]


 	self.lista = []
 	self.lista.append(["Comando", "Tiempo de CPU", "Dir. Real", "Cola de Listos","CPU", "Memoria Real", "Area swapping", "Procesos terminados" ])

 	def agregar(self, p):
 		self.lista.append([str(p.pid)],[str(p.time_created)],[str(0)], [str(0)], [str(cpu.current_process)],[ str(0)],[str(0)],[str(0)])
 		self.final[1] += p.getTime()
 		self.final[2] += 0
 		self.final[3] += 0
 		self.final[4] += 0 
 		self.final[5] += cpu.current_process
 		self.final[6] += 0 
 		self.final[7] += 0
 		self.final[8] += 0

 	def printS(self):
	     tablaResultados = tt()
	     tablaResultados.add_rows(self.final)
	     print tablaResultados.draw()

   