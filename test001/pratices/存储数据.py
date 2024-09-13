'''10-11 喜欢的数字喜欢的数字 ：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump() 将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”
'''
import json
class read_num():
    def get_user_num():
        user_num=input('请输入你最喜欢的数字：')
        fileaddress='D:/PythonProject/workspace2/test001/pratices/FileDic/num.json'
        with open(fileaddress,'w',encoding='utf-8') as num_file:
            json.dump(user_num,num_file)
            #print(num_file)
        return num_file

    def load_user_num():
        fileaddress='D:/PythonProject/workspace2/test001/pratices/FileDic/num.json'
        if fileaddress:
            with open(fileaddress,encoding='utf-8') as num:
                favarite_num=json.load(num)
                print("I know your favorite number! It's "+ favarite_num)
read_num.get_user_num()
read_num.load_user_num()


        