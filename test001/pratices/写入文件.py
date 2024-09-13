#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

#10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中
with open('FileDic/guest.txt','w',encoding='utf-8') as fileObj:
    guestspeak=input('输入一段你想啥的话，我将为你保留一万年\n')
    fileObj.write(guestspeak)

'''10-4 访客名单：编写一个while循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，
并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行'''
prompt="what is your name?"
flag=True
with open('FileDic/guest_book.txt','a',encoding='utf-8') as bookfile:
    while flag:
        username = input(prompt + '\n')
        if username=='88':
            flag=False
        else:
            bookfile.write(username+'\n')
            print('Nice to meet you '+username+'~~（ps:退出请输入：88）')


















