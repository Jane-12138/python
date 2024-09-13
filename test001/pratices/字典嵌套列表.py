#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
favorite_places={'user1':["beijin","shanghai","sichuan"],
                 'user2':["nanjin","shenzhen","england"],
                 'user3':["japan","nuowei","suzhou"]}

for name,places in favorite_places.items():
    print(name+' favorite places are : ')
    print(places[::])


favorite_nums={'s1':[1,2,3,4],
               's2':[4,5,6,7],
               's3':[9,11,23,34]}
for sname,nums in favorite_nums.items():
    print(sname+" 's favorite number are :")
    for num in nums:
        print(num)






























