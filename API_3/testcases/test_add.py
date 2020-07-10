import unittest
from API_3.common.httpRequest import HttpRequest
from API_3.common.do_excel import DoExcel
from API_3.common import constants
from ddt import ddt, data
from API_3.common.do_mysql import DoMysql
from API_3.common.context import replace

@ddt
class TestAdd(unittest.TestCase):
    excel = DoExcel(constants.case_dir, "add")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_add(self, case):
        case.data = replace(case.data)
        print(case.data)
        print(type(case.id))
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(str(case.expected), resp.json()["code"])
            self.excel.write_result(case.id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.id+1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()
