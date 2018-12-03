# Global variable to keep track of process id's.
PIDCounter = 1

class Process:

	# 's' is size in bytes
	def __init__(self, s = None, priority = None, time_created = None, page_size = 1024):
		global PIDCounter
		
		self.pid = PIDCounter
		self.size = s
		self.priority = priority
		self.time_created = time_created
		self.cpu_time = 0
		self.num_of_pages = self.size / int(page_size)
		if self.size % page_size != 0:
			self.num_of_pages += 1

		PIDCounter += 1

	def getPID(self):
		return self.pid

	def getSize(self):
		return self.size

	def getPriority(self):
		return self.priority

	def addCPUTime(self, start, end):
		self.cpu_time = self.cpu_time + (end - start)
	
	# Defines how to compare two Process objects.
	def __lt__(self, other):
		return self.priority < other.priority
