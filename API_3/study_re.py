import re
from API_3.common.config import config

# 解析正则表达式 --> 查找
data = '{"mobilephone":"#normal_user#", "pwd":"#normal_pwd#"}'
# 原本字符，元字符
p = "#(.*?)#" #正则表达式
# m = re.search(p, data) #从任意位置开始找，找第一个就返回
# print(m.group(0)) #返回表达式和组里面的内容
# print(m.group(1)) #只返回指定组的内容
# g = m.group(1) #拿到参数化的key
# v = config.get('data', g) #根据key取配置文件里面的值
# print(v)
# ms = re.findall(p, data) #查找全部，返回列表
# print(ms)
# data_new = re.sub(p, v, data, count=1) #根据p正则表达式在data中查找，并替换为v，count为替换的次数
# print(data_new)

# 如果要匹配多次，替换多次，使用循环来解决
while re.search(p, data):
    m = re.search(p, data)
    g = m.group(1)
    v = config.get('data', g)
    data = re.sub(p, v, data, count=1)

print('最后替换后的data', data)

