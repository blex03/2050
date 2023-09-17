class Entry():
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item

class PQ_UL():
    def __init__(self):
        self.L = []
        

    def __len__(self):
        return len(self.L)

    def __iter__(self):
        return iter(self.L)

    def insert(self, item, priority):
        self.L.append(Entry(item, priority))

    def find_min(self):
        min = 0
        for i in range(len(self.L)):
            if self.L[i].priority < self.L[min].priority:
                min = i
        
        
        return self.L[min]

    def remove_min(self):
        min = self.find_min()
     
        self.L.remove(min)
                

        return min

    def changepriority(self, item, newPriority):
        for i in self.L:
            if i.item == item:
                i.priority = newPriority



class PQ_OL():
    def __init__(self):
        self.L = []
    def __iter__(self):
        return iter(self.L)


    def __len__(self):
        return len(self.L)

    def insert(self, item, priority):
        self.L.append(Entry(item, priority))
        self.L.sort()

    def find_min(self):
        return self.L[0]

    def remove_min(self):
        return self.L.pop(0)

    def changepriority(self, item, newPriority):
        for i in self.L:
            if i.item == item:
                i.priority = newPriority

  








