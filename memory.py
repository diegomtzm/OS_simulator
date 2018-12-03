#Global variables
#to keep count of page_faults
page_faults = 0
#to record entrance order in memory and apply LRU 
entrance_order = 1

class Memory:

    def __init__(self, s = None, page_size = 1024, swap = None):
        self.size = s
        self.num_of_pages = self.size / int(page_size)
        if self.size % page_size != 0:
            self.num_of_pages += 1
        #tuples with (Pid, entrance_order) for LRU
        self.memory = [None] * int(self.num_of_pages)
        self.swapping = swap

    def swap_out(p):
        for i in range(self.num_of_pages):
            (x, y) = self.memory[i]
            if y == 1:
                self.swapping.insertProcess(p)
                self.memory[i] = None
                return swap_in(p, i)
            if y > 1:
                self.memory[i] == (x, y - 1)

    def swap_in(p, i):
        free = self.memory.count(None)
        self.memory[i] = (p, self.num_of_pages - free + 1)
        return i


    def loadProcess(self, p):
        loaded = False
        for i in range(self.num_of_pages):
            if self.memory[i] == None:
                if entrance_order < self.num_of_pages:
                    self.memory[i] = (p, entrance_order)
                    entrance_order += 1
                else:
                    free = self.memory.count(None)
                    self.memory[i] = (p, self.num_of_pages - free + 1)
                loaded = True
                return i

        if not loaded:
            return swap_out(p)

    def getProcessPage(self, p):
        for i in range(self.num_of_pages):
            (x, y) = self.memory[i]
            if x == p:
                return i
        return None
