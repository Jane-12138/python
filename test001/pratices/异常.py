'''10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。在这种情况下，
当你尝试将输入转换为整数时，将引发ValueError异常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
在用户输入的任何一个值不是数字时都捕获ValueError异常，并打印一条友好的错误消息。
对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字'''
'''
print('输入两个数字，帮你计算结果')
num1=input('请输入第一个数字')
num2=input('请输入第二个数字')
try:
    #将文本字符强转为整数类型，会引发ValueError,当要判断强制限制只能输入数字类型时，可以使用int()函数强转数字类型捕获错误输入
    result=int(num1)+int(num2)
except ValueError:
    print('只可输入数字！')
else:
    print('结果是'+result)

'''

'''
#10-7 加法计算器：将你为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字
print('输入两个数字，帮你计算结果')
while True:
    num1=input('请输入第一个数字')
    num2=input('请输入第二个数字')
    try:
        #将文本字符强转为整数类型，会引发ValueError,当要判断强制限制只能输入数字类型时，可以使用int()函数强转数字类型捕获错误输入
        result=int(num1)+int(num2)
    except ValueError:
        print('只可输入数字！')
        continue
    else:
        print('结果是'+str(result))
        break
'''


'''10-8 猫和狗：创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFound错误，
并打印一条友好的消息。将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。'''

cat_position='test001\pratices\FileDic\cats.txt'
dog_position='pratices\FileDic\dogs.txt'
positions=[cat_position,dog_position]
for readpositon in positions:
    try:
        with open(readpositon,'r',encoding='utf-8') as file:     
             filecontent=file.read()
    except FileNotFoundError:
        print('找不到该文件，请确认文件地址是否正确：'+readpositon)
    else: 
        print(filecontent.rstrip())


'''10-9 沉默的猫和狗：修改你在练习10-8中编写的except代码块，让程序在文件不存在时一言不发
'''

























