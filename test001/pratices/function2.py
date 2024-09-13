#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
'''
8-6 城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
这个函数应返回一个格式类似于下面这样的字符串：[插图]至少使用三个城市-国家对调用这个函数，并打印它返回的值
'''

def city_country(city,country):
    str1=city+country
    return str1

dict={'北京':'CHINA','上海':'CHINA','仙台':'Japan'}
for k,v in dict.items():
    str2=city_country(k,v)
    print(str2)






























