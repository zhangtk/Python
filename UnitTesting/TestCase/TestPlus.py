#-*- coding=utf-8 -*-

import unittest
from Count import Count

def setUpModule():
    print("setUpmModule PlusTest")

def tearDownModule():
    print("tearDownModule PlusTest")

class PlusTest(unittest.TestCase):
    '''加法测试'''
    def setUp(self):
        print("setup PlusTest")
        self.c=Count()

    def tearDown(self):
        print("tearDown PlusTest")

    @classmethod
    def setUpClass(cls):
        print("setUpClass PlusTest")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass PlusTest")

    def testPlus1(self):
        '''加法1'''
        self.assertEqual(self.c.plus(11,22),33,"different 1")
        print("testPlus1 Pass")

    def testPlus2(self):
        '''加法2'''
        self.assertEqual(self.c.plus(-2, 2), 0,"different 2")
        print("testPlus2 Pass")

    def testPlus3(self):
        '''加法3'''
        self.assertTrue(self.c.plus(-2, 2)==0,"different 3")
        print("testPlus3 Pass")

if __name__ =="__main__":
    unittest.main()