
class Swapping:

    def __init__(self, s = None, page_size = 1024):
        self.size = s
        self.num_of_pages = self.size / int(page_size)
        if self.size % page_size != 0:
            self.num_of_pages += 1
        self.swapping_area = [None] * int(self.num_of_pages)

    def insertProcess(self, p):
        if self.swapping_area.count(None) == 0:
            self.swapping_area[self.num_of_pages-1] = p
        else:
            for i in range(self.num_of_pages):
                if self.swapping_area[i] == None:
                    self.swapping_area[i] = p
                    return
