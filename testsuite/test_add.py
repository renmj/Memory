import unittest
from testsuite.basetest import BaseTest
from pageobject.addPage import AddPage
class TestModel4(BaseTest):

    def test_add(self):

        add=AddPage(self.driver)
        add.add1("JacksonYee")
        add.add2("RoyWang")
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()