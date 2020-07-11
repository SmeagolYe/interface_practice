import sys

sys.path.append('./') # project根目录地址
print(sys.path)

import unittest
from API_3.common import constants
import HTMLTestReportCN

suite = unittest.defaultTestLoader.discover(constants.cases_dir, 'test_*.py')

with open(constants.report_dir + "/report.html", "wb+") as file:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=file, title="测试报告", description="前程贷", tester="叶婷")
    runner.run(suite)