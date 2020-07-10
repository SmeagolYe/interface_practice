import unittest
from ddt import ddt, data
from API_3.common.httpRequest import HttpRequest
from API_3.common.do_excel import DoExcel
from API_3.common import constants
from API_3.common.context import replace
from API_3.common.do_mysql import DoMysql
from API_3.common import context

@ddt
class TestInvest(unittest.TestCase):
    excel = DoExcel(constants.case_dir, 'invest')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest()
        cls.mysql = DoMysql()

    @data(*cases)
    def test_invest(self, case):
        case.data = replace(case.data)
        print(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        print(resp.text)

        try:
            self.assertEqual(str(case.expected), resp.json()['code'])
            self.excel.write_result(int(case.id)+1, resp.text, "PASS")

            # 判断加标成功后，查询数据库，取到loan_id
            if resp.json()['msg'] == '加标成功':
                sql = "select id from future.loan where memberId = 1231 order by id desc limit 1"
                loan_id = self.mysql.fetchone(sql)["id"]
                print(loan_id)
                print(type(loan_id))
                #保存到类属性里面
                #从数据库中查询到的loan_id是int，要转换为str再去作替换
                setattr(context.Context, "loan_id", str(loan_id))

        except AssertionError as e:
            self.excel.write_result(int(case.id)+1, resp.text, "FAIL")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()

