#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
'''
7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；
3～12岁的观众为10美元；超过12岁的观众为15美元。
请编写一个循环，在其中询问用户的年龄，并指出其票价
'''

Flag=True
while Flag:
    age=input("你几岁了？")
    if age=='quit':
        break
    elif int(age)<=3:
        print("免费观看")
    elif 3<int(age)<=12:
        print('票价10元')
    else:
        print('票价12元')





























