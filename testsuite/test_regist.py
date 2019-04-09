import unittest
from testsuite.basetest import BaseTest
from pageobject.registpage import RegistPage
class TestModel1(BaseTest):

    def test_regist(self):

        regist = RegistPage(self.driver)
        regist.register("cshlj","cshlj@cshlj.com","1234567")
        regist.register("rmj", "rmj@rmj.com", "1234567")
        # self.assertIn("该邮箱已被注册", self.driver., "注册失败")

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()