import pymysql


class DoMysql:
    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        self.mysql = pymysql.Connect(host=host, user=user, password=password, port=port)
        # pymysql.cursors.DictCursor则查询返回的数据为字典类型，不加，则默认为元组类型
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()