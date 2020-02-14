import unittest

from parameterized import parameterized

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_com
from tools.read_data import readdata


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.api_login = ApiLogin()
    def tearDown(self) -> None:
        pass

    @parameterized.expand(readdata("login.yaml"))
    def test_login(self,username,password):

        r_login = self.api_login.apilogin(username,password)
        result = r_login.json()
        Token = result.get("data")
        #向header追加Token
        api.headers["Authorization"] = "Bearer " + Token
        print(api.headers)
        #断言
        assert_com(self,r_login)

