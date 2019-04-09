import unittest
from testsuite.basetest import BaseTest
from pageobject.archivepage import ArchivePage
class TestModel7(BaseTest):

    def test_archive(self):

        archive=ArchivePage(self.driver)
        archive.archive()
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run()