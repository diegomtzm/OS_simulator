
class ReadyQueue:

	def __init__(self):
		self.queue = []

	# Stable sorts the queue in descending order.
	def sortReadyQueue(self):
		self.queue.sort(reverse=True)

	# Gets the next process, removing it from the queue.
	def getNextProcess(self):
		if len(self.queue == 0):
			return 'empty'
		else:
			next_process = self.queue[0]
			self.queue = self.queue[1:]
			return next_process

	# Returns the next process without removing it from the queue.
	def peekNextProcess(self):
		if len(self.queue == 0):
			return 'empty'
		else:
			return self.queue[0]

	# Adds a process 'p' and sorts the queue.
	def insertProcess(self, p):
		self.queue.append(p)
		self.sortReadyQueue()

