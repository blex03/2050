from LinkedList import LinkedList

class Stack_L:
    def __init__(self):
        self._L = list()        # Composition: the Stack_L class has a List

    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List

    def push(self, item):
        self._LL.add_last(item)

    def pop(self):
        return self._LL.remove_last()
        

class Queue_L:
    def __init__(self):
        self._L = list()

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        return self._L.pop(0)

class Queue_LL:
    def __init__(self): 
        self._LL = LinkedList()

    def enqueue(self, item):
        self._LL.add_last(item)

    def dequeue(self):
        return self._LL.remove_first()

if __name__ == '__main__':
    ##########Test Stack_L##########
    stackL = Stack_L()
    
    #Push()
    element1 = 5
    stackL.push(element1)
    assert stackL._L[-1] == element1

    #Pop()
    element2 = 4
    original_stack = stackL._L
    stackL.push(element2)
    stackL.pop()
    
    assert stackL._L == original_stack

    ##########Test Stack_LL#########
    stackLL = Stack_LL()

    #Push()
    element1 = 5
    stackLL.push(element1)
    assert stackLL._LL.remove_last() == 5

    #Pop()
    element2 = 4
    original_stack = stackLL._LL
    stackLL.push(element2)
    stackLL.pop()
    assert stackLL._LL == original_stack


    ##########Test Queue_L##########
    queueL = Queue_L()

    #enqueue()
    element1 = 5
    queueL.enqueue(element1)
    assert queueL._L[-1] == element1

    #dequeue()
    element2 = 4
    queueL.enqueue(element2)
    queueL.dequeue()
    assert queueL._L[0] == 4


    ##########Test Queue_LL#########
    queueLL = Queue_LL()

    #enqueue()
    element1 = 5
    queueLL.enqueue(element1)
    assert queueLL._LL.remove_last() == 5

    #dequeue()
    element2 = 4
    queueLL.enqueue(element1)
    queueLL.enqueue(element2)
    queueLL.dequeue()
    assert queueLL._LL.remove_last() == 4