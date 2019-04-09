from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
import time
class AddPage(BaseCase):
    color_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    add_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")
    content_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    sure_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    add2_loc=(By.NAME,"添加备忘")
    def add1(self,content):
        self.click(*self.add_loc)
        self.sendkeys(content, *self.content_loc)
        self.click(*self.sure_loc)
        time.sleep(3)
    def add2(self,content):
        self.click(*self.color_loc)
        self.click(*self.add2_loc)
        self.sendkeys(content, *self.content_loc)
        self.click(*self.sure_loc)
        time.sleep(3)