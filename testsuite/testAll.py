
import unittest
import os
import HTMLTestRunner
#测试用例路径
test_dir="./"
#设置报告路径
before_dir=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(before_dir,"testreport")
if not os.path.exists(report_path):os.mkdir(report_path)
#测试内容
suite=unittest.TestLoader().discover(test_dir,pattern="test_*.py")
#运行
if __name__=="__main__":
    HTML_report = report_path + r"\report.html"
    fp = open(HTML_report, "wb")
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="单元测试报告", description="测试用例情况")
    htmlrunner.run(suite)
