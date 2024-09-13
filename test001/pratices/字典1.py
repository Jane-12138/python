#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

# favorite_num={'gakki':22,'jack':'23','rose':'24','lucy':'25'}
# for name,num in favorite_num.items():
#     print(str(name.title()) + ' favorite number is ' + str(num))

vocabulary={'if':'如果','message':'消息','else':'否则','tuple':'元祖，相当于不可修改的列表'}
for word,means in vocabulary.items():
    print(str(word.title())+
        ': \n\t'+str(means))
vocabulary['set']='集合，相当于去重的列表'
vocabulary['dict']='描述事物属性，由键值对组成'
vocabulary['number']='数字类型，普通的数字，分为整数，浮点数'
for word2,means2 in vocabulary.items():
    print(str(word2.title()) +
          ': \n\t' + str(means2))

