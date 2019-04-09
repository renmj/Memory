from framework.logger  import Logger
import os
import time
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
logger=Logger(logger="BaseCase").getlog()
class BaseCase(object):

    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
    def close(self):
        self.driver.close()
    def click(self,*loc):
        try:
            self.find_element(*loc).click()
            logger.info("点击")
        except:
            logger.error("没有点击")
    def find_element(self,*loc):
        WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except:
            logger.error("没找到")

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + '/screenshorts/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("已截图")
        except:
            self.get_windows_img()
            logger.error("截图不成功")

    #左滑
    def swipe(self,a,b,c,d,e):
        try:
            self.driver.swipe(a,b,c,d,e)
            logger.info("滑动成功")
        except:
            logger.error("滑动失败")
    # 长按
    def long_press(self, *loc):
        try:
            el = self.find_element(*loc)
            TouchAction(self.driver).long_press(el).perform()
            logger.info("长按")
        except:
            logger.error("未长按")




