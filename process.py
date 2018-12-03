# Global variable to keep track of process id's.
PIDCounter = 1

class Process:

	# 's' is size in bytes
	def __init__(self, s = None, priority = None, time_created = None):
		global PIDCounter
		
		self.pid = PIDCounter
		self.size = s
		self.priority = priority
		self.time_created = time_created
		self.num_of_pages = self.size / 1024
		if self.size % 1024 != 0:
			self.num_of_pages += 1

		PIDCounter += 1

	def getPID():
		return self.pid

	def getTime():
		return self.time_created
		
	def getSize():
		return self.size

	def getPriority():
		return self.priority
	
	# Defines how to compare two Process objects.
	def __lt__(self, other):
		return self.priority < other.priority
