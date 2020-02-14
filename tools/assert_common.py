def assert_com(self,response,status_code=200,success=True,code=10000,message="操作成功！"):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertEqual(message, response.json().get("message"))

