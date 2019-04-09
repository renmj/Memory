from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
class SearchPage(BaseCase):
    search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    content_loc=(By.ID,"android:id/search_src_text")
    def search(self,content):
        self.click(*self.search_loc)
        self.sendkeys(content, *self.content_loc)
        self.driver.keyevent(66)
