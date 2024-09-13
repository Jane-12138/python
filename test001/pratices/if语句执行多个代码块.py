#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
myfavoritefood=['cherry','grape','cherry tomato']
fruit=['apple',"banana","peach"]
fruit=fruit+myfavoritefood
print(fruit)
for value in fruit:
    if value in myfavoritefood:
        print("You really like {}!".format(value))

















































