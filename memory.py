#Global variables
#to keep count of page_faults
page_faults = 0
#to record entrance order in memory and apply LRU 
entrance_order = 1

class Memory:

    def __init__(self, s = None, page_size = 1, swap = None):
        self.size = s
        print ('mem size: "%s"' % self.size)
        self.num_of_pages = self.size / int(page_size)
        if self.size % page_size != 0:
            self.num_of_pages += 1
        print('num of pages: "%s"' % self.num_of_pages)
        #tuples with (Pid, entrance_order) for LRU
        self.memory = [(None, None)] * int(self.num_of_pages)
        self.swapping = swap

    def loadProcess(self, p):
        global entrance_order
        loaded = False
        print (self.memory)
        for i in range(self.num_of_pages):
            if self.memory[i] == (None, None):
                if entrance_order < self.num_of_pages:
                    self.memory[i] = (p, entrance_order)
                    entrance_order += 1
                else:
                    free = self.memory.count((None, None))
                    self.memory[i] = (p, self.num_of_pages - free + 1)
                loaded = True
                return i

        if not loaded:
            def swap_out(p):

                def swap_in(p, i):
                    free = self.memory.count((None, None))
                    self.memory[i] = (p, self.num_of_pages - free + 1)
                    return i

                for i in range(self.num_of_pages):
                    (x, y) = self.memory[i]
                    if y == 1:
                        self.swapping.insertProcess(p)
                        self.memory[i] = (None, None)
                        return swap_in(p, i)
                    if y > 1:
                        self.memory[i] == (x, y - 1)

            return swap_out(p)

    def getProcessPage(self, p):
        for i in range(self.num_of_pages):
            (x, y) = self.memory[i]
            if int(x) == int(p):
                return i
        return None
