import unittest
from API_3.common.httpRequest import HttpRequest
from API_3.common.do_excel import DoExcel
from API_3.common import constants
from ddt import ddt, data
from API_3.common.do_mysql import DoMysql

@ddt
class TestRegister(unittest.TestCase):
    excel = DoExcel(constants.case_dir, "register")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_register(self, case):
        print(case.data)
        if case.data.find("register_mobile") > -1:
            sql = "select max(mobilephone) from future.member"
            register_mobile = int(self.mysql.fetchone(sql)[0]) + 100
            case.data = case.data.replace("register_mobile", str(register_mobile))

        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.id+1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
