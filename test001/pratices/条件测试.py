#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

name_list=["Gakki","jack","rose","zhuliye"]
new_name=input("猜猜被抽中的人是谁：")
#无论大小写，不允许相同
if new_name in name_list:
    if new_name=="jack":
        print("you are false")
    elif new_name=="rose":
        print("you are false")
    elif new_name=="zhuliye":
        print("no no no")
    else :
        print("you are right")
else:
    print("sorry")








































