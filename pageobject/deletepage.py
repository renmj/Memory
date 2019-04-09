from  pageobject.basepage  import BaseCase
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
class DeletePage(BaseCase):
    note_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_all")
    delete_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")
    color_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    look_loc=(By.NAME,"回收站")
    null_loc=(By.NAME,"清空回收站")
    sure_loc=(By.NAME,"确定")
    def delete(self):
        self.long_press(*self.note_loc)
        self.click(*self.delete_loc)
        self.click(*self.color_loc)
        self.click(*self.look_loc)
        self.click(*self.null_loc)
        self.click(*self.sure_loc)
