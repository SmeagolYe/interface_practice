import unittest
from API_3.common.httpRequest import HttpRequest
from API_3.common import constants
from API_3.common.do_excel import DoExcel
from ddt import ddt, data
from API_3.common.do_mysql import DoMysql

@ddt
class TestRegister(unittest.TestCase):
    excel = DoExcel(constants.case_dir, "recharge")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_recharge(self, case):
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetchone(sql)
            print(member)
            before_amount = member['LeaveAmount']

        resp = self.http_request.request(case.method, case.url, case.data)
        print(resp.json())
        try:
            self.assertEqual(str(case.expected), resp.json()["code"])
            self.excel.write_result(case.id+1, resp.text, "PASS")
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetchone(sql)
                after_amount = member['LeaveAmount']
                recharge_amount = float(eval(case.data['amount']))
                # 充值判断，数据库校验
                self.assertEqual(before_amount + recharge_amount, after_amount)
        except AssertionError as e:
            self.excel.write_result(case.id+1, resp.text, "FAIL")
            return e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()