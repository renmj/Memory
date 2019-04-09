import unittest
from testsuite.basetest import BaseTest
from pageobject.searchpage import SearchPage
class TestModel5(BaseTest):

    def test_search(self):

        search=SearchPage(self.driver)
        search.search("TFBOYS")
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()