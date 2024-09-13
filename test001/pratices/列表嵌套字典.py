#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
vocabulary={'if':'如果','message':'消息','else':'否则','tuple':'元祖，相当于不可修改的列表'}
Gakki={'high':'160cm','hobby':'reading','ido':'Yuzuru Hanyu'}
Yuzuru={'high':'172cm','hobby':'skating','color':'blue'}

lis=[vocabulary,Gakki,Yuzuru]
for users in lis:
    for property,value in users.items():
        print(property+' : '+value)















































