import re
import configparser
from API_3.common.config import config


class Context:
    loan_id = None


def replace(data):
    p = "#(.*?)#"
    while re.search(p, data):
        m = re.search(p, data)
        g = m.group(1)
        try:
            v = config.get('data', g)
        # 如果配置文件里面没有的时候，去context里面取
        except configparser.NoOptionError as e:
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print("找不到参数化的值")
                raise e

        data = re.sub(p, v, data, count=1)

    return data
