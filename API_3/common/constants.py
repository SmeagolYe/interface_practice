import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Excel用例的路径
case_dir = os.path.join(base_dir, 'data', 'cases.xlsx')

global_conf_dir = os.path.join(base_dir, 'config', 'global.conf')
online_conf_dir = os.path.join(base_dir, 'config', 'online.conf')
test_conf_dir = os.path.join(base_dir, 'config', 'test.conf')

log_dir = os.path.join(base_dir, 'log', 'case.log')

# 代码case的路径
cases_dir = os.path.join(base_dir, "testcases")

report_dir = os.path.join(base_dir, "reports")