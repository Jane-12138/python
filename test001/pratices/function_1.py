#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

'''
8-1 消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
'''

def display_message(a):
    print('本章将学习：'+a.title())


'''
8-3 T恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样
'''

def make_shirt(size,content='I love Python'):
    print('想要一件'+size+'的衣服，且打印有'+content)
# display_message('function')
make_shirt('大号')
make_shirt('中号')
make_shirt('大号','i hate you')


'''
8-4 大号T恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
调用这个函数来制作如下T恤：
一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
'''

'''
8-5 城市：编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如Reykjavik is in Iceland。
给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''
def describe_city(city,country='China'):
    #注意：默认形参要放最后，不要放在非默认形参前面
    print(city+' is in '+country)

describe_city(city='珠海')
describe_city(city='北京')
describe_city(city='纽约',country='America')















































































