import logging
import logging.handlers
import os

import api
from config import filepath


class GetLogger(object):
    __logger = None
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            logger_path = filepath + os.sep + "log" + os.sep + "time.log"
            # 获取日志器
            cls.__logger = logging.getLogger()

            # 设置日志器level
            cls.__logger.setLevel(level=logging.INFO)

            # 设置按照时间分隔日志的处理器
            lhth = logging.handlers.TimedRotatingFileHandler(filename=logger_path,
                                                             when="midnight",
                                                             interval=1,
                                                             backupCount=3,
                                                             encoding="utf-8")
            # 设置格式器
            fm = logging.Formatter(fmt="%(asctime)s %(levelno)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)- %(message)s")
            # 将格式器添加到处理器中
            lhth.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(lhth)
        return cls.__logger

if __name__ == '__main__':
    GetLogger.get_logger().info("buzh")
