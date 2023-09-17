# TODO: init, gt, eq
class Entry:
    def __init__(self, priority, item):
        """Initializes Entry Variables"""
        self.priority = priority
        self.item = item


    def __gt__(self, other):
        """returns True if line of priority is greater than other"""
        for i in range(min(len(self.priority), len(other.priority))):
            if self.priority[i] > other.priority[i]:
                return True
            elif other.priority[i] > self.priority[i]:
                return False

        if len(self.priority) > len(other.priority):
            return True
        else:
            return False
        

    def __eq__(self, other):
        """returns True if priority lines are equal"""
        return self.priority == other.priority

    # repr is provided for you
    def __repr__(self):
        """Returns string representation of an Entry """
        return f"Entry(priority={self.priority}, item={self.item})"



# TODO: _heapify_up, _heapify_down, put, remove_max
class MaxHeap:
    # init is provided for you, but you should modify the default `heapify_direction` value
    def __init__(self, items=None, heapify_direction='up'):
        """Initializes a new MaxHeap with optional collection of items"""
        self._L = []

        # if a collection of items is passed in, heapify it
        if items is not None:
            self._L = list(items)
            if heapify_direction == 'up': self._heapify_up()

            elif heapify_direction == 'down': self._heapify_down()

            else: raise RuntimeError("Replace `heapify_direction` default with 'up' or 'down' instead of `None`")

    def _heapify_up(self):
        """Heapifies self._L in-place using only upheap"""
        index = 0
        parent = self._parent(index)
        
        while parent is not None and self._L[index] > self._L[parent]:
            self._L[index], self._L[parent] = self._L[parent], self._L[index]
            index = parent
            parent = self._parent(index)


    def _heapify_down(self):
        """Heapifies self._L in-place using only downheap"""
        index = 0
        min_index = self.min_child(index)

        while min_index is not None and self._L[index] < self._L[min_index]:
            self._L[min_index], self._L[index] = self._L[index], self._L[min_index]
            index = min_index
            min_index = self.min_child(index)

    def put(self, entry):
        """Inserts element into heap"""
        self._L.append(entry)

    def remove_max(self):
        """removes max from heap"""
        if not self._L:
            raise RuntimeError("Heap is Empty")

        max = 0
        for i in range(len(self._L)):
            if self._L[i].priority > self._L[max].priority:
                max = i

        max = self._L[max]

        self._L.remove(max)

        return max.item
        
    # len is number of items in PQ
    def __len__(self):
        """Number of items in PQ"""
        return len(self._L)

    #TODO: Add any private helper functions (e.g. _left, _right, _upheap, ...) below
    def _parent(self, i):
        return (i-1) // 2
    
    def _left(self, i):
        return 2*i + 1
    
    def _right(self, i):
        return 2*i + 2

    def min_child(self, i):
        left = self._left(i)
        right = self._right(i)
        if right is None: 
            return left
        try:
            if self._L[left] < self._L[right]:
                return left
            else:
                return right
        except IndexError:
            return None