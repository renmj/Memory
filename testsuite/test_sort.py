import unittest
from testsuite.basetest import BaseTest
from pageobject.sortpage import SortPage
class TestModel6(BaseTest):

    def test_sort(self):

        sort=SortPage(self.driver)
        sort.sort()
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()