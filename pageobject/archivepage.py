from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
import time
class ArchivePage(BaseCase):
    note_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_all")
    archive_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")
    color_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    look_loc=(By.NAME,"归档")
    huifu_loc=(By.NAME,"恢复")
    def archive(self):
        time.sleep(5)
        self.long_press(*self.note_loc)
        self.click(*self.archive_loc)
        self.click(*self.color_loc)
        self.click(*self.look_loc)
        time.sleep(5)
        self.swipe(629,111,530,111,1000)
        self.click(*self.huifu_loc)

