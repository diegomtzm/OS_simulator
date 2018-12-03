
class ReadyQueue:

	def __init__(self):
		self.queue = []

	# p is the process added to the ready queue.
	def insert(self, p):
		self.queue.append(p)
		sortReadyQueue()

	def sortReadyQueue(self):
		self.queue.sort(reverse=True)

	def getNextProcess(self):
		process = self.queue[0]
		# Reduce queue by one.
		self.queue = self.queue[1:]
		if(process is not None):
			return process
		else:
			return 'empty'
