# coding: UTF-8
import random  # 导入随机函数random模块，这样下面才能使用random函数产生随机数

try:  # try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
    f = open('D://old_no.txt')  # 测试能否打开这个文件来判断文件是否存在
    f.close()  # 文件打开了就必须要关闭
except IOError:  # 判断是否出现IOError这个错误信息，如果出现，则说明那个文件不存在
    print("此前的随机数据不存在，现在将新建随机数据储存文件。")
    file = open('D://old_no.txt', 'a')  # 新建一个数据储存文件，参数a表示打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
else:  # 如果上面判断语句没发现IOError这个错误信息，则运行以下内容
    # -------------------------------此处开始为读取文件内容并生成列表，然后将str的列表转换成int格式--------------------------------------------------
    file_read = open('D://old_no.txt')  # 再次打开文件读取文件内容，如果直接用file_read的话，内容为空，因为前面已经使用了
    list_no = []  # 建立空白列表
    for line in file_read.readlines():  # 读取文件内容并且用reallines()函数生成列表形式
        list_no.append(list(map(int, line.split(','))))   # 将每行内容添加进列表，用'，'隔开，这样生成的列表里面每个字符都是子列表
    # print("list_no={}".format(list_no))
    list_no_change = str(list_no).replace('[', '').replace(']', '').replace(' ', '')  # 用replace函数将子列表的"["&"]"&"空格"去掉，但是列表每个值还是字符串形式
    # print(list_no_change)  # 输出字符串
    list_no_ok = list(eval(list_no_change))  # 应用强大的eval函数转义将字符串型转换成数据型，然后再将转义后的列表用list函数生成列表，再保存替换原来的列表中
    # print('之前保存的数据为:{}'.format(list_no_ok))  # 输出int格式的列表
    # print("{}的格式为{}".format(list_no_ok[0],type(list_no_ok[0])))# 显示列表第一个值的格式为int
    set_no = set(list_no_ok)
    print('之前保存的数据为:{}'.format(set_no))  # 输出int格式的集合
    file_read.close()  # 文件打开了就必须要关闭-----------------------------自此，成功将文件内容读出并转换为int格式的集合-----------------------------

'''
    ------------------------------------------------在界面角落提供“重置”按钮，如果要清除之前的数据请按按钮-------------------------------------
print("确认要重置数据吗？是/否")#按下按钮后，弹出确认框，是对应True，否对应False，并赋值给reset_button按钮
if reset_button==True:
    file=open('D://old_no.txt','w')
    file.close()
elif reset_button==False:
    pass
    -----------------------------------------------------------------以上为多行注释来屏蔽GUI界面的功能----------------------------------------
'''
'''
    ---------------------------------每次随机数据暂存内存，需要的话点击“保存”按钮写入到文件里，下次打开再点击读取---------------------------------
file=open('D://old_no.txt','a')#打开数据文件准备写入，参数a表示新内容将会被写入到已有内容之后
    ----------------------------------------------------------------以上为多行注释来屏蔽GUI界面的功能-----------------------------------------
'''

min_no_input = input('请输入想随机的起始数字:')  # 提示输入数据
max_no_input = input('请输入想随机的结尾数字:')
min = min_no_input.isnumeric()  # 检测输入的数据是否全部由数字组成
max = max_no_input.isnumeric()

while min is False or max is False or float(min_no_input) >= float(max_no_input):  # 如果输入的数字不是全部由数字组成或者起始数字大于等于结尾数字，则进入循环--注意：由于min_no_input和max_no_input由input函数赋值，是str字符串格式，所以要比较他们的大小，必须先把格式化为浮点数型
    print('你好，你输入的内容不是整数，或者起始数字大于等于结尾数字，请重新输入。')
    min_no_input = input('请输入想随机的起始数字:')  # 提示输入数据
    max_no_input = input('请输入想随机的结尾数字:')
    min = min_no_input.isnumeric()
    max = max_no_input.isnumeric()  # 检测输入的数据是否全部由数字组成
    if min is True and max is True and float(min_no_input) < float(max_no_input):  # 如果输入的数字全部由数字组成且起始数字小于结尾数字
        break  # 退出循环

min_no = round(float(min_no_input))  # 由于input函数输入的是str字符串型，必须转换为整数型才能进行随机运算，直接用int转换的话提示错误，所以先用float转换为浮点型，然后再用round取整去小数点
max_no = round(float(max_no_input))
random_no = random.randint(min_no, max_no)  # 产生范围内的随机数

if random_no not in set_no:  # 判断随机数是否已存在，如果不存在则写入集合
    print('新的随机数生成：' + str(random_no))  # 调试用的输出
    set_no.add('random_no')  # 随机数写入集合
else:
    while random_no in set_no:  # 判断随机数是否已存在，如果存在则重新产生随机数直到不存在
        print(str(random_no) + '：已经存在')  # 调试用的输出
        random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
    else:  # 经过循环重新产生不存在的随机数，然后写入集合
        print('新的随机数生成：' + str(random_no))  # 调试用的输出
        set_no.add('random_no')  # 随机数写入集合
# -----------------------------------------------自此，成功产生随机数并写入集合--------------------------------------------------
'''
     -----------------------------------------------每次点击“随机”按钮运行下面代码产生随机数并写入集合内-----------------------------
random_no = random.randint(min_no, max_no)  # 产生范围内的随机数

if random_no not in set_no:  # 判断随机数是否已存在，如果不存在则写入集合
    print('新的随机数生成：' + str(random_no))  # 调试用的输出
    set_no.add('random_no')  # 随机数写入集合
else:
    while random_no in set_no:  # 判断随机数是否已存在，如果存在则重新产生随机数直到不存在
        print(str(random_no) + '：已经存在')  # 调试用的输出
        random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
    else:  # 经过循环重新产生不存在的随机数，然后写入集合
        print('新的随机数生成：' + str(random_no))  # 调试用的输出
        set_no.add('random_no')  # 随机数写入集合
    --------------------------------------------------以上为多行注释来屏蔽GUI界面的功能---------------------------------------------
'''
# 以下编写将集合写入数据文件的代码
