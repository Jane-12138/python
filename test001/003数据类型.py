#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
'''一个整数占32位，id()获取数值的占位'''
# a=1
# b=2
# c=123
# a1=id(a)
# b1=id(b)
# c1=id(c)
# print("a的内存占位是%d"%a1+",,轮到b的占位是%d"%b1)
# print(c1)

# import math
# a=1.23
# b=1.23
# a = math.ceil(a)
# b = math.floor(b)
# type(b)
# type(a)
# print(type(a))
# print(a+b)


# print(max(a))
# print(min(a))

# print(type(None))

a=1
b=2
print("****%d"%(a+b))

#字符串
c="abcdef gijklnm"
# print(c[2])
# print(len(c))   #获取字符串长度1
# print(c[-1])    #获取字符串最后一个字符
# print(c[len(c)-1])  #获取字符串最后一个字符2

#字符串切片数据
print(c[0:6:2])     #截取a到f，每隔1个取1个，用冒号分隔；a是开始位置，b是截止位置，c是步长
print(c[6:])   #第二个参数不写，表示取全部
print(c[6:-1])  #第一和二个参数为-1时，表示取最后一个，-2是取最后一个的前一个
print(c[0:6:1])     #第三个参数是步长，每一步取一个
print(c[::-2])     #c是负数，则是倒着取，第1、2个参数不写，表示取全部

#字符串相关函数
dd="helloword 123 how long will i love you a soundthand year?"
res1=dd.find("123")  #找到某字符串的第一次出现时的下标  object.find("某字符串")
res2=dd.rfind("123")    #找到某字符串的最后一次出现的下标 object.rfind("某字符串")
res3=dd.find("kkk")     #find函数查找不存在的字符串会返回-1
print(res1,res2,res3)
print(dd.index("123"))  
print(dd.rindex("123"))     #index函数和find函数效果一样，区别是对于不存在的字符串find会返回-1，index会报错
# print(dd.index("kkk"))








