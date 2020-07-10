import requests


class HttpRequest:
    def request(self, method, url, data=None, json=None, cookies=None):
        if method.lower() == "get":
            resp = requests.get(url, params=data, cookies=cookies)
        elif method.lower() == "post":
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            print("Unsupported method")
        return resp


class HttpRequest2:
    def __init__(self):
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        if method.lower() == "get":
            resp = self.session.request(method=method, url=url, params=data)
        elif method.lower() == "post":
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp = None
            print("unsupported method")
        return resp

    def close(self):
        self.session.close() #必须关闭session，不然数据会一直在内存中
