#-*- coding=utf-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
from TestPlus import PlusTest

suite = unittest.TestSuite()
suite.addTest(PlusTest("testPlus1"))
suite.addTest(PlusTest("testPlus2"))
suite.addTest(PlusTest("testPlus3"))

file = open("Result.html", "wb")
runner = HTMLTestRunner(stream=file, title='单元测试报告', description='用例执行情况：')
runner.run(suite)

file.close()
