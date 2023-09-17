import unittest
from TaskQueue import Task, TaskQueue

class TestTask(unittest.TestCase):
    def test_init(self):
        t1 = Task(1, 3)
        self.assertEqual(t1.id, 1)
        self.assertEqual(t1.cycles_left, 3)
        self.assertEqual(t1.next, None)
        self.assertEqual(t1.prev, None)

    def reduce_cycles(self):
        t1 = Task(1, 3)
        t1.reduce_cycles()
        self.assertEqual(t1.cycles_left, 2)

class TestTaskQueue(unittest.TestCase):
    def test_init(self):
        tq1 = TaskQueue()
        self.assertEqual(tq1.cycles_per_task, 1)
    
    def test_add__remove_task(self):
        tq1 = TaskQueue()

        t1 = Task(1, 3)
        t2 = Task(2, 3)
        t3 = Task(3, 3)

        tq1.add_task(t1)
        tq1.add_task(t2)
        tq1.add_task(t3)

        self.assertEqual(tq1.current, t1)
        self.assertEqual(tq1.current.next, t2)
        self.assertEqual(tq1.current.next.next, t3)
        self.assertEqual(tq1.current.prev, t3)
        self.assertEqual(tq1.current.prev.prev, t2)

        tq1.remove_task(1)
        self.assertEqual(tq1.current, t2)
        
        tq1.remove_task(2)
        self.assertEqual(tq1.current, t3)

        tq1.remove_task(3)
        self.assertEqual(tq1.current, None)

        with self.assertRaises(RuntimeError):
            tq1.remove_task(4)
        

    def test__len__(self):
        tq1 = TaskQueue()

        t1 = Task(1, 3)
        t2 = Task(2, 3)
        t3 = Task(3, 3)

        tq1.add_task(t1)
        tq1.add_task(t2)
        tq1.add_task(t3)

        self.assertEqual(len(tq1), 3)

    def test_empty(self):
        tq1 = TaskQueue()
        t1 = Task(1, 3)
        tq1.add_task(t1)

        self.assertEqual(tq1.is_empty(), False)

        tq1.remove_task(1)

        self.assertEqual(tq1.is_empty(), True)

    def test_execute(self):
        tq1 = TaskQueue()

        t1 = Task(1, 3)
        t2 = Task(2, 1)
        t3 = Task(3, 5)

        tq1.add_task(t1)
        tq1.add_task(t2)
        tq1.add_task(t3)

        self.assertEqual(tq1.execute_tasks(), 9)
        




unittest.main() # runs all unittests above