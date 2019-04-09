from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
from framework.util import Util

class LoginPage(BaseCase):
    color_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    login_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    email_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    login_btn_loc=(By.NAME,"登录")
    def login(self,email,pwd):
        self.click(*self.color_loc)
        self.click(*self.login_loc)
        self.sendkeys(email,*self.email_loc)
        self.sendkeys(pwd, *self.pwd_loc)
        self.click(*self.login_btn_loc)