#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

#计算总和
lis=[]
for value in range(1,1000000):
    lis.append(value)
lis_sum=sum(lis)
lis_max=max(lis)
lis_min=min(lis)
print("总和是:%d"%lis_sum)
print(lis_max)
print(lis_min)

#奇数
lis2=[]
for value2 in range(1,20,2):
    lis2.append(value2)
print(lis2)

#4-7 3的倍数
lis3=[value3*3 for value3 in range(3,21)]
print(lis3)

#立方解析
lis4=[value4**2 for value4 in range(1,11)]
print("立方解析结果:{}".format(lis4))


