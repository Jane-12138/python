#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
checklists1=["学委","贝贝","文文"]
outman=checklists1[2]
print(outman+"女士将在下一站下车")

#修改列表元素
checklists1[2]="不灵"
print("新的人生旅车将包括："+str(checklists1))

checklists1.insert(0,"巴子")
checklists1.insert(2,"冰冰")
checklists1.append("Yuzuru")

print("新的嘉宾包括："+str(checklists1))

p1=checklists1.pop(2)
print(checklists1)
p2=checklists1.pop(2)
print(checklists1)
p3=checklists1.pop(0)
print(checklists1)
print("soryy，i can't eat with you "+p1)
del checklists1[0]
del checklists1[1]
del checklists1[2]
print(checklists1)