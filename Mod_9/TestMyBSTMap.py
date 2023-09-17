import unittest, random
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """Tests that equal magic method returns True when trees are equal when empty"""
        t1 = MyBSTMap()
        t2 = MyBSTMap()

        self.assertEqual(t1 == t2, True)


    def test_equal_multiplenodes(self):
        """Tests that equal magic method returns True when trees are equal with multiple nodes"""
        t1 = MyBSTMap()
        t2 = MyBSTMap()
        '''t1
                          9: '9'
                        /       \
                   6:'6'      50: '50'  
                   / 
                3:'3' 
        '''

        t1.put(9, '9')
        t1.put(50, '50')
        t1.put(6, '6')
        t1.put(3, '3')

        '''t2
                          9: '9'
                        /       \
                   6:'6'      50: '50'  
                   / 
                3:'3' 
        '''
        t2.put(9, '9')
        t2.put(50, '50')
        t2.put(6, '6')
        t2.put(3, '3')

        self.assertEqual(t1 == t2, True)


    def test_notequal_multiplenodes_difshapes(self):
        """Tests that eq magic method returns false when keys and values are the same but the shape is different"""
        t1 = MyBSTMap()
        t2 = MyBSTMap()

        '''t1
                          9: '9'
                        /       \
                   3:'3'      50: '50'  
                      \ 
                        6:'6' 
        '''

        t1.put(9, '9')
        t1.put(3, '3')
        t1.put(6, '6')
        t1.put(50, '50')

        '''t2
                          9: '9'
                        /       \
                   6:'6'      50: '50'  
                   / 
                3:'3' 
        '''
        t2.put(9, '9')
        t2.put(6, '6')
        t2.put(3, '3')
        t2.put(50, '50')

        self.assertEqual(t1 == t2, False)

    
    def test_notequal_multiplenodes_difkvs(self):
        """Tests that eq magic method returns false when keys and values are different"""
        t1 = MyBSTMap()
        t2 = MyBSTMap()

        '''t1
                3: '3'
                    \
                    9: '9'  
                    /   \
                6:'6'   50:'50'
        '''

        t1.put(3, '3')
        t1.put(9, '9')
        t1.put(6, '6')
        t1.put(50, '50')

        '''t2
                3: '3'
                    \
                    10:'10'  
                    /   \
                7:'7'   50:'50'
        '''

        t2.put(3, '3')
        t2.put(10, '10')
        t2.put(7, '7')
        t2.put(50, '50')

        self.assertEqual(t1 == t2, False)

    def test_frompreorder_small(self):
        """Tests that correct binary search tree is generated from preordered list"""

        '''bst1
                3: '3'
                    \
                    24: '24'  
                    /   \
                22:'22'   2003:'2003'
        '''


        bst1 = MyBSTMap()
        for k in [3, 24, 2003, 22]: 
            bst1.put(k, str(k))

        L = [(k, v) for (k, v) in bst1.preorder()]
        bst2 = MyBSTMap.frompreorder(L) 
        self.assertEqual(bst1 == bst2, True)

    def test_frompreorder_large(self):

        """Tests that correct binary search tree is generated from postordered list"""
        bst1 = MyBSTMap()
        nums = [i for i in range(100)]
        random.shuffle(nums)
        for k in nums: 
            bst1.put(k, str(k))

        L = [(k, v) for (k, v) in bst1.preorder()] 
        bst2 = MyBSTMap.frompreorder(L)
        self.assertEqual(bst1 == bst2, True)

    def test_frompostorder_small(self):

        """ADD DOCSTRING"""


        '''bst1
                3: '3'
                    \
                    24: '24'  
                    /   \
                22:'22'   2003:'2003'
        '''

        bst1 = MyBSTMap()
        for k in [3, 24, 2003, 22]: 
            bst1.put(k, str(k))

        L = [(k, v) for (k, v) in bst1.postorder()] 
        bst2 = MyBSTMap.frompostorder(L)
        self.assertEqual(bst1 == bst2, True)

    def test_frompostorder_large(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        nums = [i for i in range(100)]
        random.shuffle(nums) 
        for k in nums: 
            bst1.put(k, str(k))

        L = [(k, v) for (k, v) in bst1.postorder()] 
        bst2 = MyBSTMap.frompostorder(L) 
        self.assertEqual(bst1 == bst2, True)

unittest.main()