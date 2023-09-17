# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0): 
        '''Initializes Function'''
        self.pos = (round(pos[0], precision), round(pos[1], precision))
        self.max = max
        self.min = min
        self.precision = precision

    def add_report(self, temp): 
        '''Sets min and max temperatures'''
        if self.max == None:
            self.max = temp
        if self.min == None:
            self.min = temp
        elif temp > self.max:
            self.max = temp
        elif temp < self.min:
            self.min = temp

    def __eq__(self, other):
        '''Returns True(False) if positions of instances are(are not) equal'''
        return self.pos == other.pos
        
    def __hash__(self): 
        '''Hashes position'''
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self):
        '''Initializes function'''
        self._n_buckets = 5
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def __len__(self):
        '''returns number of position tuples in instance''' 
        return self._len

    def add_report(self, pos, temp):
        '''adds position and updates temperature'''
        record = LocalRecord(pos)
        index = hash(record.pos) % self._n_buckets
        if record.pos in self:
            for i in self._L[index]:
                if i.pos == record.pos: 
                    i.add_report(temp)
        else:
            self._L[index].append(record)
            record.add_report(temp)

            self._len += 1
        
        if len(self) / self._n_buckets >= 0.75:
            self._rehash(self._n_buckets * 2)

    def __getitem__(self, pos):
        '''determine if pos is in Record'''
        record = LocalRecord(pos) 
        if record.pos not in self:
            raise KeyError("Position not in Map")
        else:
            index = hash(pos) % self._n_buckets
            for i in self._L[index]:
                if i.pos == record.pos:
                    return i.min, i.max
             

  
    def __contains__(self, pos): 
        record = LocalRecord(pos)
        index = hash(record.pos) % self._n_buckets
        for i in self._L[index]:
            if i.pos == record.pos:
                return True
        return False
            

    def _rehash(self, m_new): 
        new_list = [[] for i in range(m_new)] 
        self._n_buckets = m_new

        for bucket in self._L:
            for item in bucket:
                index = hash(item) % self._n_buckets
                new_list[index].append(item)

        # Update self._L to point to the new list
        self._L = new_list