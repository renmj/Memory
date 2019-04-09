from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
class ModifyPage(BaseCase):
    color_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    user_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    biaofu_loc=(By.ID,"com.pdswp.su.smartcalendar:id/imageView4!")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    sure_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    def modify(self,name):
        self.click(*self.color_loc)
        self.click(*self.user_loc)
        self.click(*self.biaofu_loc)
        self.sendkeys(name, *self.name_loc)
        self.click(*self.sure_loc)
