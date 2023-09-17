from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self): 
        """Create graph in setUp so it only needs to be defined once"""
        self.Vs = {"New York", "Hartford", "Berlin", "Beijing", "Tokyo"}
        self.Es = {"New York": {"Hartford": 117, "Berlin": 3965}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                   "Beijing": {"Berlin": 4571, "Tokyo": 1300},  "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                   "Hartford": {"Tokyo": 6705, "New York": 117}}
        

        
        self.g = Graph(self.Vs, self.Es)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    #New York, Hartford, Tokyo, Beijing, Berlin

    '''          3,965 mi          4,571 mi
        New York------------Berlin----------Beijing
          |                                   |
    117 mi|                                   | 1,300 mi
          |                                   |
        Hartford----------------------------Tokyo
                           6,705 mi
    '''

    def testInitializer(self):
        '''Test that given vertices and edges are added to V and nbrs correctly'''
        self.assertEqual(self.g._V, self.Vs)
        self.assertEqual(self.g._nbrs, self.Es)

    def testAddRemoveVertex(self):
        '''Tests that we can add and remove a few vertices from the graph'''
        self.g.remove_vertex("Hartford")
        self.assertEqual(self.g._V, {"New York", "Berlin", "Beijing", "Tokyo"})

        self.g.remove_vertex("Tokyo")
        self.assertEqual(self.g._V, {"New York", "Berlin", "Beijing"})

        with self.assertRaises(KeyError):
            self.g.remove_vertex("Tokyo")

        self.g.add_vertex("Hartford")
        self.assertEqual(self.g._V, {"New York", "Berlin", "Beijing", "Hartford"})

        self.g.add_vertex("Tokyo")
        self.assertEqual(self.g._V, {"New York", "Berlin", "Beijing", "Hartford", "Tokyo"})

    def testAddRemoveEdge(self):
        '''Tests that we can add and remove a few edges from the graph'''
        self.g.remove_edge("New York", "Berlin", 3965)
        self.g.remove_edge("Beijing", "Tokyo", 1300)

        self.assertEqual(self.g._nbrs, {"New York": {"Hartford": 117}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                                        "Beijing": {"Berlin": 4571},  "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                                        "Hartford": {"Tokyo": 6705, "New York": 117}})
                                   
        with self.assertRaises(KeyError):
            self.g.remove_edge("Berlin", "Beijing", 4572)

        with self.assertRaises(KeyError):
            self.g.remove_edge("Beijing", "Tokyo", 1300)

        self.g.remove_edge("Beijing", "Berlin", 4571)

        with self.assertRaises(KeyError):
            self.g.remove_edge("Beijing", "Berlin", 4571)

        self.g.add_edge("New York", "Berlin", 3965)
        self.assertEqual(self.g._nbrs, {"New York": {"Hartford": 117, "Berlin": 3965}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                                        "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                                        "Hartford": {"Tokyo": 6705, "New York": 117}})

        self.g.add_edge("Beijing", "Tokyo", 1300)
        self.assertEqual(self.g._nbrs, {"New York": {"Hartford": 117, "Berlin": 3965}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                                        "Beijing": {"Tokyo": 1300},  "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                                        "Hartford": {"Tokyo": 6705, "New York": 117}})

    def testNbrs(self):
        '''Tests that nbrs returns an iterater that produces neighboring cities'''
        nbr_set = set()

        for nbr in self.g.nbrs("Hartford"):
            nbr_set.add(nbr)

        self.assertEqual(nbr_set, {"Tokyo", "New York"})

        self.g.remove_edge("Hartford", "Tokyo", 6705)

        nbr_set = set()

        for nbr in self.g.nbrs("Hartford"):
            nbr_set.add(nbr)
        
        self.assertEqual(nbr_set, {"New York"})

    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self): 
        """Create graph in setUp so it only needs to be defined once"""
        self.Vs = {"New York", "Hartford", "Berlin", "Beijing", "Tokyo"}
        self.Es = {"New York": {"Hartford": 117, "Berlin": 3965}, "Berlin": {"New York": 3965, "Beijing": 4571},  
                   "Beijing": {"Berlin": 4571, "Tokyo": 1300},  "Tokyo": {"Beijing": 1300, "Hartford": 6705},
                   "Hartford": {"Tokyo": 6705, "New York": 117}}
        

        
        self.g = Graph(self.Vs, self.Es)


    # TODO: Which alg do you use here, and why?
    # Alg: Breadth First Search
    # Why: The algorithm finds the least number of edges to each vertex

    def test_fewest_flights(self):
        """Tests that fewest_flights returns the shortest path with least number of flights to each city"""
        x = self.g.fewest_flights('Hartford')[1]
        self.assertEqual(x, {'Hartford': 0, 'Tokyo': 1, 'New York': 1, 'Beijing': 2, 'Berlin': 2})

        x = self.g.fewest_flights('Tokyo')[1]
        self.assertEqual(x, {'New York': 2, 'Berlin': 2, 'Beijing': 1, 'Hartford': 1, 'Tokyo': 0})

        x = self.g.fewest_flights('Berlin')[1]
        self.assertEqual(x, {'Tokyo': 2, 'New York': 1, 'Hartford': 2, 'Beijing': 1, 'Berlin': 0})
 
 # TODO: Which alg do you use here, and why?
    # Alg: Dijkra's Algorithm
    # Why: Finds the shortest path to each vertex

    def test_shortest_path(self):
        """tests that shortest_path returns the shortest path with shortest distance to each city"""
        x = self.g.shortest_path('Hartford')[1]
        self.assertEqual(x, {'Hartford': 0, 'Tokyo': 6705, 'New York': 117, 'Beijing': 8005, 'Berlin': 4082})

        x = self.g.shortest_path('Tokyo')[1]
        self.assertEqual(x, {'New York': 6822, 'Berlin': 5871, 'Beijing': 1300, 'Hartford': 6705, 'Tokyo': 0})

        x = self.g.shortest_path('Berlin')[1]
        self.assertEqual(x, {'Tokyo': 5871, 'New York': 3965, 'Hartford': 4082, 'Beijing': 4571, 'Berlin': 0})

 # TODO: Which alg do you use here, and why?
    # Alg: Prim's Algorithm
    # Why: Prim's finds the shortest path to connect all of the vertices


    def test_minimum_salt(self):
        "tests that minimum_salt returns the shortest path that connects all of the verticies"

        x = self.g.minimum_salt('Hartford')[1]
        self.assertEqual(x, {'Hartford': 0, 'Tokyo': 1300, 'New York': 117, 'Beijing': 4571, 'Berlin': 3975})

        x = self.g.minimum_salt('Tokyo')[1]
        self.assertEqual(x, {'New York': 3975, 'Berlin': 4571, 'Beijing': 1300, 'Hartford': 117, 'Tokyo': 0})

        x = self.g.minimum_salt('Berlin')[1]
        self.assertEqual(x, {'Tokyo': 1300, 'New York': 3965, 'Hartford': 117, 'Beijing': 4571, 'Berlin': 0})


unittest.main()