from MaxHeap import Entry, MaxHeap
import unittest, random, time
random.seed(658)

#TODO: Fill out any empty tests below
class TestEntry(unittest.TestCase):

    def test_gt_onepriority(self):
        """Tests Entry's with 1 priority"""
        e1 = Entry([0], "zero")
        e2 = Entry([1], "one")

        self.assertEqual(e2 > e1, True)
        self.assertEqual(e1 > e2, False)
        self.assertEqual(e1 > e1, False)


    def test_gt_threepriorities(self):
        """Tests Entries with with 3 priorities"""
        e1 = Entry([0, 'f', 42.3], "zero")
        e2 = Entry([1, 'g', 14], "one")
        e3 = Entry([0, 'f', 42.1], "two")
        e4 = Entry([0, 'g', 14], "three")

        self.assertEqual(e2 > e1, True)
        self.assertEqual(e1 > e3, True)
        self.assertEqual(e2 > e4, True)
        self.assertEqual(e4 > e1, True)


        self.assertEqual(e1 > e2, False)
        self.assertEqual(e3 > e1, False)
        self.assertEqual(e4 > e2, False)
        self.assertEqual(e1 > e4, False)

    def test_gt_mismatchedpriorities(self):
        """Test comparisons b/w entries with different numbers of priorities"""
        e1 = Entry([0, 'f', 42.3], "zero")
        e2 = Entry([0, 'g'], "one")
        e3 = Entry([0, 'f', 42.1, 0], "two")
        e4 = Entry([0, 'g', 14, 12], "three")

        self.assertEqual(e2 > e1, True)
        self.assertEqual(e1 > e3, True)
        self.assertEqual(e4 > e2, True)
        self.assertEqual(e4 > e1, True)


        self.assertEqual(e1 > e2, False)
        self.assertEqual(e3 > e1, False)
        self.assertEqual(e2 > e4, False)
        self.assertEqual(e1 > e4, False)


    def test_eq(self):
        """Test that items w/ exact same priorities are seen as equal"""

        e1 = Entry([0, 'g', 14, 12], "three")
        e2 = Entry([0, 'g', 14, 12], "three")
        e3 = Entry([0, 'g', 14], "three")

        self.assertEqual(e1 == e2, True)
        self.assertEqual(e1 == e3, False)


     
class TestMaxHeap(unittest.TestCase):
    def test_add_remove_single(self):
        """Add a single item to the max heap, then remove it. This test is provided for you as an example."""
        e1 = Entry(priority=[0], item="jake")
        mh = MaxHeap()
        self.assertEqual(len(mh), 0)
        mh.put(e1)
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove_max(), "jake")

    def test_add_remove_random(self):
        """Add and remove many random items w/ same number of priorities"""
        entryList = [Entry([1], "one"), Entry([2], "two"), Entry([3], "three"), Entry([4], "four"), Entry([5], "five")]      
        mh = MaxHeap()
        random.shuffle(entryList)

        for i in entryList:
            mh.put(i)

        self.assertEqual(len(mh), 5)

        self.assertEqual(mh.remove_max(), "five")
        self.assertEqual(mh.remove_max(), "four")
        self.assertEqual(mh.remove_max(), "three")
        self.assertEqual(mh.remove_max(), "two")
        self.assertEqual(mh.remove_max(), "one")
        self.assertEqual(len(mh), 0)


    def test_add_remove_several(self):
        """Add and remove several items with different numbers of priorities"""
        e1 = Entry([0, 'g', 3], "one")
        e2 = Entry([0, 'g', 2], "two")
        e3 = Entry([0, 'g', 3, 18], "three")
        e4 = Entry([0, 'g', 2, 20], "four")
        mh = MaxHeap()

        self.assertEqual(len(mh), 0)

        mh.put(e1)
        mh.put(e2)
        mh.put(e3)
        mh.put(e4)

        self.assertEqual(len(mh), 4)
        self.assertEqual(mh.remove_max(), "three")
        self.assertEqual(mh.remove_max(), "one")
        self.assertEqual(mh.remove_max(), "four")
        self.assertEqual(mh.remove_max(), "two")
        self.assertEqual(len(mh), 0)

    def test_removefromempty(self):
        """Test Runtime error when removiung from empty"""
        mh = MaxHeap()
        with self.assertRaises(RuntimeError):
            mh.remove_max()

    # NOTE: This times heapify_up and _down, but does not test their functionality
    def test_heapify(self):
        """Times heapify up and heapify down approaches. This 'test' provided for you"""
        print() # an extra blank line at the top
        
        # table header
        print('='*40)
        print(f"{'n':<10}{'t_h_up (ms)':<15}{'t_h_down (ms)':<15}"   )
        print('-'*40)

        # table body
        scalar = int(1E3)
        for n in [i*scalar for i in [1, 2, 3, 4, 5]]:
            t_h_up = 1000*time_f(MaxHeap, (list(range(n)), 'up'))
            t_h_down = 1000*time_f(MaxHeap, (list(range(n)), 'down'))
            print(f"{n:<10}{t_h_up:<15.2g}{t_h_down:<15.2g}")

        # table footer
        print("-"*40)

def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(*args)
        end = time.time()
        if end-start < t_min: t_min = end - start

    return t_min
unittest.main()