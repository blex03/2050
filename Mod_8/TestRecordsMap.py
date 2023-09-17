
from operator import getitem
import unittest
from RecordsMap import LocalRecord, RecordsMap
# Import what you need
# Include unittests here. Focus on readability, including comments and docstrings.

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """test intilizer variables"""
        record1 = LocalRecord((43.5, 16.3))
        self.assertEqual(record1.pos, (44, 16))
        self.assertEqual(record1.min, None)
        self.assertEqual(record1.max, None)
        self.assertEqual(record1.precision, 0)

    def test_hash(self):
        """test hash magic method"""
        record1 = LocalRecord((43.5, 16.3))
        self.assertEqual(hash(record1), hash((44, 16)))

    def test_eq(self):
        """Test that eq returns True iff two records are in the same position"""
        record1 = LocalRecord((43.5, 16.3))
        record2 = LocalRecord((43.5, 16.3))
        record3 = LocalRecord((15.1, 27.8))

        self.assertEqual(record1 == record2, True)
        self.assertEqual(record1 == record3, False)
 

    def test_add_report(self):
        """test that max and min are correctly updated"""
        record1 = LocalRecord((43.5, 16.3))
        record1.add_report(15)
        record1.add_report(47)
        self.assertEqual(record1.max, 47)
        self.assertEqual(record1.min, 15)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """test RecordsMap when one position is added"""
        map1 = RecordsMap()

        #add_report and contains
        self.assertEqual((34, 23) in map1, False)
        map1.add_report((34.0, 23.1), 47)
        self.assertEqual((34, 23) in map1, True)

        #len
        self.assertEqual(len(map1), 1)

        #get
        self.assertEqual(map1[(34, 23)], (47, 47))
        

    def test_add_many_reports(self):
        """test RecordsMap when many many position are added"""
        map1 = RecordsMap()

        #add_report and contains
        self.assertEqual((34, 23) in map1, False)

        map1.add_report((34.0, 23.1), 47)
        self.assertEqual((34, 23) in map1, True)

        map1.add_report((34.0, 23.1), 54)
        self.assertEqual((34, 23) in map1, True)

        map1.add_report((52.9, 91.2), 13)
        self.assertEqual((53, 91) in map1, True)

        #len
        self.assertEqual(len(map1), 2)

        #get
        self.assertEqual(map1[(34.1, 23.0)], (47, 54))

        map1.add_report((34.0, 23.1), 53)
        self.assertEqual(map1[(34.1, 23.0)], (47, 54))

        map1.add_report((34.0, 23.1), 55)
        self.assertEqual(map1[(34.1, 23.0)], (47, 55))






# You need to add a line here to run the unittests
unittest.main()