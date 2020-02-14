import unittest

import api
from api.api_employees import ApiEmployees
from tools.assert_common import assert_com
from parameterized import parameterized


from tools.read_data import readdata


class TestEmployees(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_employees = ApiEmployees()
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(readdata("employees.yaml"))
    def test01_post(self,username,mobile,workNumber):
        r = self.api_employees.api_post_employee(username,mobile,workNumber)
        assert_com(self,r)
        api.user_id = r.json().get("data").get("id")
        print(api.user_id)

    def test02_put(self):
        r = self.api_employees.api_put_employee(username="qqgg",mobile="12345678912",workNumber="12345678")
        assert_com(self, r)

    def test03_get(self):
        r = self.api_employees.api_get_employee()
        assert_com(self, r)

    def test04_post(self):
        r = self.api_employees.api_delete_employee()
        assert_com(self, r)
