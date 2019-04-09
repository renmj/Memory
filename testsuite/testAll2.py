import unittest
import HTMLTestRunner
import os
from testsuite.test_add import TestModel4
from testsuite.test_search import TestModel5

#设置报告路径
cur_dir=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(cur_dir,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

#构建测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestModel5))
suite.addTest(unittest.makeSuite(TestModel4))

#运行并生成报告
if __name__=="__main__":

    HTML_report=report_path+r"\report.html"
    fp=open(HTML_report,"wb")
    htmlrunner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="测试用例情况")

    # runner=unittest.TextTestRunner(verbosity=2)
    htmlrunner.run(suite)