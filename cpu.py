import ready_queue as rq
import time

class CPU:

	# Initialize CPU with ready queue
	def __init__(self):
		self.ready_q = rq.ReadyQueue()
		self.current_process = None
		self.process_start_time = time.time()

	# Gets a process from the ready queue into the CPU
	# Checks whether there is a higher priority Process in queue and swaps.
	def compete(self):
		if self.current_process is None:
			try:
				next_process = self.ready_q.getNextProcess()
				if next_process != 'empty':
					# Begin timer for process.
					self.process_start_time = time.time()
					self.current_process = process
			except:
				pass
		elif checkFrontQueue():
			next_process = self.ready_q.getNextProcess()
			
			# Adds the time it was in the CPU.
			self.current_process.addCPUTime(time.time(), self.process_start_time)
			self.ready_q.insertProcess(self.current_process)

			# Begin timer for next process.
			self.process_start_time = time.time()
			self.current_process = next_process

	# Checks if the process that was inserted into queue has higher priority than cur proc.
	def checkFrontQueue(self):
		next_process = self.ready_q.peekNextProcess()
		return next_process.priority > self.current_process.priority

	# Adds process to the queue and competes for CPU.
	def addProcess(self, p):
		self.ready_q.insertProcess(p)
		self.compete()


