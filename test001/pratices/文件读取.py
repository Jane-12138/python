#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子

#相对路径访问:同当前运行文件所在目录同级或下一级文件、目录，注意路径开头不需要斜杠，win10路径不需要反斜杠\，而是用斜杠/
# read()方法读取文件全部内容
#当出现编码错误时，open函数内可传入参数：encoding='gbk', errors='ignore'
with open('test001/pratices/FileDic/test1.txt',encoding='utf-8') as testfile:
    fileContent=testfile.read()
    print(fileContent.rstrip())

#绝对路径访问
#for遍历文件
filename='D:/PythonProject/workspace2/test001/pratices/FileDic/test1.txt'
with open(filename,encoding='utf-8') as file:
    for fileContent2 in file:
        print(fileContent2.rstrip())

#readlines()读取文件各行并输出列表
with open('D:/PythonProject/workspace2/test001/pratices/FileDic/test1.txt',encoding='utf-8') as readfile:
    fileContent3=readfile.readlines()
fileSum=''
for fileAll in fileContent3:
    fileSum+=fileAll.strip()
print(fileSum)