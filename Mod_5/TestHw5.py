from hw5 import valid_moves, solveable
import unittest

class TestValidMoves(unittest.TestCase):
        def testValidMoves(self):
                """Tests that valid_moves returns correct positions"""
                # 'k' denotes a knight
                # 'x' denotes possible moves
                # Positions should be given in (row, column) tuples
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - x - - - - - -
                #6 - - x - - - - -
                #7 k - - - - - - -
                # TODO: Fill in the data to test valid_moves on the board above
                k_idx = (7, 0)
                expected_valid_moves = {(5, 1), (6, 2)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                # TODO: Write tests for valid_moves for the following boards
                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - x - - - - -
                #2 - x - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                
                k_idx = (0, 0)
                expected_valid_moves = {(2, 1), (1, 2)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - k
                #1 - - - - - x - -
                #2 - - - - - - x -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
                
                k_idx = (0, 7)
                expected_valid_moves = {(1, 5), (2, 6)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - - - - - - -
                #2 - - - - - - - -
                #3 - - - - - - - -
                #4 - - - - - - - -
                #5 - - - - - - x -
                #6 - - - - - x - -
                #7 - - - - - - - k
                
                k_idx = (7, 7)
                expected_valid_moves = {(6, 5), (5, 6)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
 
                k_idx = (3, 3)
                expected_valid_moves = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}
                self.assertEqual(valid_moves(k_idx), expected_valid_moves)

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                self.assertEqual(solveable({(2, 4), (3, 1), (6, 6)}, (1, 2)), False) 
                self.assertEqual(solveable({(2, 1), (0, 1), (0, 2)}, (3, 3)), False) 

        def testSolveableSimple(self):
                self.assertEqual(solveable({(2, 1), (4, 2)}, (0, 0)), True)

        def testSolveableHard(self):
                self.assertEqual(solveable({(2, 1), (4, 2), (2, 3), (1, 1)}, (0, 0)), True)

                #  0 1 2 3 4 5 6 7
                #0 k - - - - - - -
                #1 - - p - - - - -
                #2 - - - - p - - -
                #3 - - p - - - - -
                #4 - p - - - - - -
                #5 - - p p - - - -
                #6 p - - - - - - -
                #7 - - - - - - - -

                self.assertEqual(solveable({(1, 2), (2, 4), (3, 2), (4, 1), (5, 2), (5, 3), (6, 0)}, (0, 0)), True)

                
                

unittest.main()