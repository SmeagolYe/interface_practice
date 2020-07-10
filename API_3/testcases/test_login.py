import unittest
from API_3.common.httpRequest import HttpRequest
from API_3.common.do_excel import DoExcel
from API_3.common import constants
from ddt import ddt, data
from API_3.common import logger

mylogger = logger.get_logger(__name__)

@ddt
class TestLogin(unittest.TestCase):
    excel = DoExcel(constants.case_dir, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        mylogger.info("准备测试前置")
        cls.http_request = HttpRequest()

    @data(*cases)
    def test_login(self, case):
        mylogger.info("开始测试第{0}条用例：{1}".format(case.id, case.title))
        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.id+1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case.id+1, resp.text, "FAIL")
            mylogger.error("报错了，{0}".format(e))
            raise e
        mylogger.info("结束测试第{0}条用例：{1}\n".format(case.id, case.title))

    @classmethod
    def tearDownClass(cls):
        mylogger.info("测试后置处理")
        cls.http_request.close()
