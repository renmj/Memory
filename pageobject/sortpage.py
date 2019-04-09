from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
import time
class SortPage(BaseCase):
    note_loc = (By.ID, "com.pdswp.su.smartcalendar:id/note_all")
    sort_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_sort")
    sure_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")
    def sort(self):
        time.sleep(5)
        self.long_press(*self.note_loc)
        time.sleep(3)
        self.click(*self.sort_loc)
        time.sleep(3)
        self.swipe(624,498,624,306,1000)
        self.click(*self.sure_loc)
