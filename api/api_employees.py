import requests

import api


class ApiEmployees(object):
    def __init__(self):
        #url
        self.post_url = api.host +  "/api/sys/user"
        self.put_url = api.host + "/api/sys/user/{}"
        self.get_url = api.host + "/api/sys/user/{}"
        self.delete_url = api.host + "/api/sys/user/{}"
    def api_post_employee(self,username,mobile,workNumber):
        data = {"username":username,"mobile":mobile,"workNumber":workNumber}
        return requests.post(self.post_url,json=data,headers=api.headers)
    def api_put_employee(self,username,mobile,workNumber):
        data = {"username":username,"mobile":mobile,"workNumber":workNumber}
        return requests.put(self.put_url.format(api.user_id),json=data,headers=api.headers)
    def api_get_employee(self):
        return requests.get(self.get_url.format(api.user_id),headers=api.headers)
    def api_delete_employee(self):
        return requests.delete(self.delete_url.format(api.user_id),headers=api.headers)