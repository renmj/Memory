from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
class RegistPage(BaseCase):
    color_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    regist1_loc=(By.NAME,"点击注册备忘录云平台")
    regist2_loc=(By.NAME,"注册一个吧!")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    email_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    regist_btn_loc=(By.NAME,"注册")
    def register(self,name,email,pwd):
        self.click(*self.color_loc)
        self.click(*self.regist1_loc)
        self.click(*self.regist2_loc)
        self.sendkeys(name, *self.name_loc)
        self.sendkeys(email,*self.email_loc)
        self.sendkeys(pwd, *self.pwd_loc)
        self.click(*self.regist_btn_loc)
