import unittest
import os
from HTMLTestRunner import HTMLTestRunner


#创建测试集
suite = unittest.TestSuite()

#获取加载器
loader = unittest.defaultTestLoader

#寻找匹配的用例
cases = loader.discover(os.getcwd(),pattern="Test*.py")
#添加到测试集里
suite.addTest(cases)
# 创建HTML运行器
f=open("计算器测试报告.html", "w+", encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title="计算器加减乘除法报告",
    description="这是一个计算器加减乘除法的报告",
    verbosity=1
)
# 4.用运行器运行测试集
runner.run(suite)

