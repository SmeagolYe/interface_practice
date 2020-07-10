import pymysql

# 1.建立连接：数据库的连接信息
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
# 2.获取游标
cursor = mysql.cursor()
# 3.编写sql语句
sql = "select max(mobilephone) from future.member"
# 4.执行sql语句
cursor.execute(sql)
# 5.查看结果
result = cursor.fetchone()
# result = cursor.fetchall()
print(result)
# 6.关闭查询
cursor.close()
# 7.关闭数据库连接
mysql.close()