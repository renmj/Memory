import logging
import time
import os
class Logger():
    def __init__(self,logger):
    # 创建logger对象
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #定义两种handle用于写入日志文件
        date=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"
        log_name=log_path+date+".log"

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        #定义输出格式，用formater
        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #为logger添加Headler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return  self.logger


