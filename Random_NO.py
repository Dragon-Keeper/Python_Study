# -*- coding: UTF-8 -*-
import random #导入随机函数random模块，这样下面才能使用random函数产生随机数

try:#try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
    f =open('D://old_no.txt')#测试能否打开这个文件来判断文件是否存在
    f.close()#文件打开了就必须要关闭
except IOError:#判断是否出现IOError这个错误信息，如果出现，则说明那个文件不存在
    print("此前的随机数据不存在，现在将新建随机数据储存文件。")
    file=open('D://old_no.txt','a')#新建一个数据储存文件，参数a表示打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
else:#如果上面判断语句没发现IOError这个错误信息，则运行以下内容
    file_read=open('D://old_no.txt')#打开文件
    all_no_read=file_read.read()#读取打开的文件内容
    print('此前的随机数据内容如下:'+all_no_read)#输出文件内容
    file_read.close()#文件打开了就必须要关闭

'''
    ---------------------------------------------------------------------以下为多行注释来屏蔽GUI界面的功能------------------------------------------
#在界面角落提供“重置”按钮，如果要清除之前的数据请按按钮
print("确认要重置数据吗？是/否")#按下按钮后，弹出确认框，是对应True，否对应False，并赋值给reset_button按钮
if reset_button==True: 
    file=open('D://old_no.txt','w')
    file.close()
elif reset_button==False:
    pass
    ---------------------------------------------------------------------以上为多行注释来屏蔽GUI界面的功能------------------------------------------
'''
'''
每次随机数据暂存内存，需要的话点击“保存”按钮写入到文件里，下次打开再点击读取。
'''

'''--------------------------------不需要这个定义函数来写入文件了，现在暂时以列表(list)/集合(set)形式存放在内存，在点击“保存”按钮后才写入数据文件----------
def text_in_txt(msg):#定义函数用于写入数据到数据文件里
    full_path='D://old_no.txt'#数据文件位置&文件名
    file=open(full_path,'a')#打开数据文件进入写入状态
    file.write(str(msg))#传递函数数据写入数据文件
    file.write('\n')#输入回车，让下次的随机数据输入到下一行
    file.close()#文件打开了就必须要关闭
    print('内容写入完毕:'+str(random_no))#提示文件写入完毕并显示写入的数据内容
'''
#注意——————————上面的random_no是函数，在按下“保存”按钮后将内存中的随机数据写入数据保存文件，否则留在内存不保存——————————注意
 
min_no_input=input('请输入想随机的起始数字:')#提示输入数据
max_no_input=input('请输入想随机的结尾数字:')
min=min_no_input.isnumeric()#检测输入的数据是否全部由数字组成
max=max_no_input.isnumeric()

while min==False or max==False or float(min_no_input)>=float(max_no_input) :#如果输入的数字不是全部由数字组成或者起始数字大于等于结尾数字，则进入循环--注意：由于min_no_input和max_no_input由input函数赋值，是str字符串格式，所以要比较他们的大小，必须先把格式化为浮点数型
    print('你好，你输入的内容不是整数，或者起始数字大于等于结尾数字，请重新输入。')
    min_no_input=input('请输入想随机的起始数字:')#提示输入数据
    max_no_input=input('请输入想随机的结尾数字:')
    min=min_no_input.isnumeric()
    max=max_no_input.isnumeric()#检测输入的数据是否全部由数字组成
    if min==True and max==True and float(min_no_input)<float(max_no_input):#如果输入的数字全部由数字组成且起始数字小于结尾数字
        break#退出循环
    
min_no=round(float(min_no_input))#由于input函数输入的是str字符串型，必须转换为整数型才能进行随机运算，直接用int转换的话提示错误，所以先用float转换为浮点型，然后再用round取整去小数点
max_no=round(float(max_no_input))
random_no=random.randint(min_no,max_no)#产生范围内的随机数
#text_in_txt(random_no)#通过前面定义的函数text_in_tex传递数据并写入数据文件---------------不需要了

#取消上面数据写入数据文件内再提取比较方法，用Python的列表(list)/集合(set)

#重写字典文件写入txt和从txt文件读取成为列表(list)/集合(set)：平时随机数据写入列表(list)/集合(set)，按下“保存”按钮后写入txt，否则随软件关闭丢失。已保存的数据可以在“读取”按钮后读取