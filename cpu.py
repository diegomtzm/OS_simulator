import ready_queue as rq

class CPU:

	# Initialize CPU with ready queue
	def __init__(self):
		self.ready_q = rq.ReadyQueue()
		self.current_process = None

	# Gets a process from the ready queue into the CPU
	# Checks whether there is a higher priority Process in queue and swaps.
	def compete(self):
		if self.current_process is None:
			try:
				next_process = self.ready_q.getNextProcess()
				if next_process != 'empty':
					self.current_process = process
			except:
				pass
		elif checkFrontQueue():
			next_process = self.ready_q.getNextProcess()
			self.ready_q.insertProcess(self.current_process)
			self.current_process = next_process

	# Checks if the process that was inserted into queue has higher priority than cur proc.
	def checkFrontQueue(self):
		next_process = self.ready_q.peekNextProcess()
		return next_process.priority > self.current_process.priority

	# Adds process to the queue and competes for CPU.
	def addProcess(self, p):
		self.ready_q.insertProcess(p)
		self.compete()


