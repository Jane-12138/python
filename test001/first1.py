# name=input("your name is ?")
# age=int(input("your age is?"))
# print("your name is:%s"%name)
# print("and your age is:%s"%age)
# print(type(age))
# print(name,age,end="**")
print(divmod(10,3))
a=False==1
print(a)
a=2
a+=2
print(a)

##逻辑运算符
'''
and 与运算：
a and b, 两头都为数字时，取后者b
a=false,b=true时;a and b, 结果为false

or 或运算
a=1,b=2;a and b ; 取前者a
a=false;b=true; a and b; 结果为true

not 非运算
not 布尔值 ，取反
not 非0数值，结果都为false；
因为只有0==false，not 0 输出true;只有1==true,not 1 结果为false

'''

'''
成员运算符
in 判断某个值是否在序列或列表中，在的话，返回true,不在返回false
not in 不在列表中
'''
a=[1,2,3]
i=2
if i in a:
    print("b是a的成员")
else:
    print("b不是其中一员")
print("---------------------------------------------------------------")

#身份运算符
'''
is 判断两个标识在存储内容上是否来自同一个对象
== 是判断两个的数值上是否相同
is not 判断两个标识存储内容上是否是来自不同对象
'''
aa1=1
bb=1.0
print(aa1 is bb)
print(aa1==bb)
print("---------------------------------------------------------------")


'''
三目运算符，常用！！
常规是：
a>b ? a:b  表示：？号前面的条件为真时，执行冒号前的步骤，为假时，执行冒号后面的步骤 
但python不一样：python是：
为真执行动作  if  判断条件  else  为假执行动作
'''
x=5
y=1
x=x+1 if x>y else x-1
print(x)

