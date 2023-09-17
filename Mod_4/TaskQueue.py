class Task:
    def __init__(self, id, cycles_left, next = None, prev = None):
        self.id = id
        self.cycles_left = cycles_left
        self.next = next
        self.prev = next
    
    def reduce_cycles(self, cycles_removed):
        self.cycles_left -= cycles_removed

class TaskQueue:
    def __init__(self, cycles_per_task = 1):
        self.cycles_per_task = cycles_per_task
        self.current = None
        self.length = 0
        self.id_set = set()

    def add_task(self, task):
        if self.current == None:
            self.current = task
            self.current.next = self.current
            self.current.prev = self.current
        
        else:
            self.current.prev.next = task
            task.next = self.current
            task.prev = self.current.prev
            self.current.prev = task

        self.length += 1
        self.id_set.add(task.id)



    def remove_task(self, id):
        if id not in self.id_set:
            raise RuntimeError(f"'{id}' does not exist in Task Queue")

        original = self.current
        node = self.current
        while node.id != id:
            node = node.next

        node.prev.next = node.next
        node.next.prev = node.prev

        self.length -= 1
        self.id_set.remove(node.id)

        if self.is_empty():
            self.current = None

        elif node.id == self.current.id:
            self.current = self.current.next
        

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0

    def execute_tasks(self):
        cycle_count = 0

        while not self.is_empty():
            self.current = self.current.next
                
            if self.current.prev.cycles_left <= self.cycles_per_task:
                cycle_count += self.current.prev.cycles_left
                self.current.prev.reduce_cycles(self.current.prev.cycles_left)

            elif self.current.prev.cycles_left > self.cycles_per_task:
                cycle_count += self.cycles_per_task
                self.current.prev.reduce_cycles(self.cycles_per_task)
                

            if self.current.prev.cycles_left <= 0:
                print(f"Finished task {self.current.prev.id} after {cycle_count} clock cycles")
                self.remove_task(self.current.prev.id)
    
                

        return cycle_count
                    
                

    