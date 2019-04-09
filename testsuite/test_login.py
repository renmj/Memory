import unittest
from testsuite.basetest import BaseTest
from pageobject.loginpage import LoginPage
from framework.util import Util
class TestModel2(BaseTest):

    def test_login(self):
        el = Util.read_excel("E:/workspace/Memorandum/data/info.xlsx", "Sheet1")
        login = LoginPage(self.driver)
        login.login(el[0]["user"],el[0]["pwd"])
        # login.login(el[1]["user"],el[1]["pwd"])
        # self.assertIn("该邮箱已被注册", self.driver., "注册失败")

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()