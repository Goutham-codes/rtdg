'''
File : test.py
Function : create and run testcases to test the cli functions
Authors : Gouthaman,Aditya,kalaiyarasu
'''


# import statements
import unittest
import os
from cli import checkinputs, writedata, all_func


class TestApp(unittest.TestCase):
    def test_inputs(self):
        # test for input validation
        # args for test case  : no. of fields, total no. of records, filepath
        test_case_1 = (8, 100, '/home/project/test1.csv')
        test_case_2 = (11, 100, '/home/project/test1.csv')
        test_case_3 = (8, 1000, '/home/project/test1.csv')
        test_case_4 = (8, 100, '/home/project/test1.jpeg')
        self.assertTrue(checkinputs(*test_case_1))
        self.assertRaises(ValueError, checkinputs, *test_case_2)
        self.assertRaises(ValueError, checkinputs, *test_case_3)
        self.assertRaises(ValueError, checkinputs, *test_case_4)

    def test_write(self):
        # test for writing data
        # args for test case  : filepath, total no. of records,
        # fields, functions
        path1 = os.path.join(os.getcwd(), 'test1.csv')
        test_case_1 = (path1, 100, ['city', 'coordinate'], [
                       all_func['address']['city'],
                       all_func['geo']['coordinate']])
        self.assertTrue(writedata(*test_case_1))


if __name__ == '__main__':
    unittest.main()
