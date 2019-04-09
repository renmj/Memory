# -*- coding:utf-8 -*-
import os.path
import yaml
from appium import webdriver
from framework.logger  import Logger

#创建一个日志记录器实例
logger=Logger(logger="AndroidEngine").getlog()

class AndroidEngine(object):

    def appium_desired(self):
        dir = os.path.dirname(os.path.abspath("."))  # 相对路径获取方法
        print(dir)
        with open(dir+'\config\config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        desired_caps = {}
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['sessionOverride'] = data["sessionOverride"]
        desired_caps['app'] =dir+data['app']
        desired_caps['noReset'] = data['noReset']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return driver

    def quit_android(self):
        logger.info("关闭APP")
        self.driver.quit()
# el=AndroidEngine()
# el.appium_desired()