from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                board1 = [3, 0, 0, 5, 0, 0, 0, 0, 0]
                self.assertEqual(puzzle(board1), True)

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                board1 = [1, 0, 0, 0, 0]
                self.assertEqual(puzzle(board1), True)

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                board1 = [3, 6, 4, 1, 3, 4, 2, 0]
                self.assertEqual(puzzle(board1), True)
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                board1 = [3, 4, 1, 2, 0]
                self.assertEqual(puzzle(board1), False)

unittest.main()