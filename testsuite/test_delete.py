import unittest
from testsuite.basetest import BaseTest
from pageobject.deletepage import DeletePage
class TestModel8(BaseTest):

    def test_delete(self):

        delete=DeletePage(self.driver)
        delete.delete()
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()