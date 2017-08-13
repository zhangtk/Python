import unittest
import time
from HTMLTestRunner import HTMLTestRunner
dir='./'

discover = unittest.defaultTestLoader.discover(dir,'Test*.py')

if __name__=="__main__":
    now = time.strftime("%Y%m%d_%H%M%S")
    filename = "Resulat_" +now+".html"
    file = open(filename,"wb")
    runner = HTMLTestRunner(stream=file,title='单元测试报告',description='用例执行情况：')
    runner.run(discover)

    file.close()
