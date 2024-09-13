#设置模板
#这样每个.py文件都会有这串注释了
#加油啊，柚子
'''
8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
'''

def make_album(single_name,music_name):
    dict={music_name:single_name}
    print(dict)

make_album('周杰伦','牛仔很忙')
make_album('周杰伦','甜甜的')
make_album('周杰伦','花海')

















