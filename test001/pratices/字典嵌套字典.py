#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

citys={'qinyuan':{'country':'China','population':'200万','fact':'很山卡拉，科技不发达'},
       'xiantai':{'country':'Japan','population':'60万','fact':'羽生结弦的故乡'},
       'suzhou':{'country':'China','population':'700万','fact':'很美，江南水乡'}}
for city,discrition in citys.items():
    print('About {} : '.format(city.title()))
    for k,v in discrition.items():
        print("\t"+k+' : '+v)

for n in range(0,10):
    citys[n]={'country':'Japan','population':'60万','fact':'羽生结弦的故乡'}
for x,y in citys.items():
    print(x)
    print(y)





















