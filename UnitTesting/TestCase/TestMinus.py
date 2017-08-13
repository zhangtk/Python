#-*- coding=utf-8 -*-

import unittest
from Count import Count

def setUpModule():
    print("setUpmModule MinusTest")

def tearDownModule():
    print("tearDownModule MinusTest")

class MinusTest(unittest.TestCase):
    '''减法测试'''
    def setUp(self):
        print("setup MinusTest")
        self.c=Count()

    def tearDown(self):
        print("tearDown MinusTest")

    @classmethod
    def setUpClass(cls):
        print("setUpClass MinusTest")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass MinusTest")

    def testMinus1(self):
        '''减法1'''
        self.assertEqual(self.c.minus(11,22),-11,"different 1")
        print("testPlus1 Pass")

    def testMinus2(self):
        '''减法2'''
        self.assertEqual(self.c.minus(2, 2), 0,"different 2")
        print("testPlus2 Pass")

    def testMinus3(self):
        '''减法3'''
        self.assertTrue(self.c.minus(2, 2)==0,"different 3")
        print("testPlus3 Pass")

if __name__ =="__main__":
    unittest.main()