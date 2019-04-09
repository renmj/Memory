import  unittest
import warnings
from framework.android_engine import AndroidEngine
class BaseTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        jdriver = AndroidEngine()
        self.driver=jdriver.appium_desired()

        print("开始")
    def tearDown(self):
        self.driver.quit()
        print("结束")