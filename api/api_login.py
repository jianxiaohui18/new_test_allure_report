import requests

import api
from tools.get_log import GetLogger

log = GetLogger.get_logger()
class ApiLogin(object):
    def __init__(self):
        self.login_url = api.host +  "/api/sys/login"
        log.info("开始初始化登录url：{}".format(self.login_url))
    def apilogin(self,mobile,pwd):
        data = {"mobile":mobile, "password":pwd}
        return requests.post(url=self.login_url,json=data,headers=api.headers)