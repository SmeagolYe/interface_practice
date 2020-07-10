import requests
from API_3.common.config import config
from API_3.common import logger

mylogger = logger.get_logger(__name__)


class HttpRequest:
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.lower()

        if type(data) == str:
            data = eval(data)

        url = config.get('api', 'pre_url') + url
        mylogger.debug("请求url：{0}".format(url))
        mylogger.debug("请求data：{0}".format(data))

        if method == "get":
            resp = self.session.request(method=method, url=url, params=data)
        elif method == "post":
            if data:
                resp = self.session.request(method=method, url=url, data=data)
            else:
                resp = self.session.request(method=method, url=url, json=json)
        else:
            resp = None
            mylogger.error("输入的请求method非post或get")

        mylogger.debug("请求response:{0}".format(resp.text))
        return resp

    def close(self):
        self.session.close()

