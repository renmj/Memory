import unittest
from testsuite.basetest import BaseTest
from pageobject.loginpage import LoginPage
from pageobject.modifyPage import ModifyPage
class TestModel3(BaseTest):

    def test_modify(self):
        #
        # login = LoginPage(self.driver)
        # login.login("cshlj@cshlj.com","1234567")

        modify=ModifyPage(self.driver)
        modify.modify("rmj")

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()