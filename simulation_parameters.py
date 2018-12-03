class SimulationParameters:

	# Initialize simulation parameters as class variables to None for later modification
	# once simulation starts.
	def __init__(self, schedule_p = 'PrioExp', mem_p = 'LRU', q = None, 
		         real_mem = None, swap_mem = None, p_size = 1):

		self.schedule_policy = schedule_p
		self.memory_policy = mem_p
		self.quantum = q
		self.real_memory = real_mem
		self.swap_memory = swap_mem
		self.page_size = p_size
