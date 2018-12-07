# coding: UTF-8
import random  # 导入随机函数random模块，这样下面才能使用random函数产生随机数
import os  # 导入os模块，os模块包含普遍的操作系统功能
import linecache  # 该模块允许从任何文件里得到任何的行，并且使用缓存进行优化，常见的情况是从单个文件读取多行。

set_no = set()  # 生成空白集合，否则后面生成的随机数无法合法写入集合，因为集合还没有被定义

try:  # try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
    f = open('old_no.txt')  # 测试能否打开这个文件来判断文件是否存在,默认当前目录
    f.close()  # 文件打开了就必须要关闭
except IOError:  # 判断是否出现IOError这个错误信息，如果出现，则说明那个文件不存在
    print("此前的随机数据不存在，现在将新建随机数据储存文件。")
    file = open('old_no.txt', 'a')  # 新建一个数据储存文件，参数a表示打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
else:  # 如果上面判断语句没发现IOError这个错误信息，则运行以下内容

    # -------------------------------此处开始为读取文件内容并生成列表，然后将str的列表转换成int格式--------------------------------------------------

    # 以下代码为判断文件内容是否为空，如果是空的话则跳过下面的步骤，直接到输入起始数字位置--------------------------------------------------------------
    size = os.path.getsize('old_no.txt')  # 判断文件内容是否为空
    if size != 0:  # 判断文件内容不为空，则打开文件读取内容并转化成int格式集合
        file_read = open('old_no.txt')  # 再次打开文件读取文件内容，如果直接用file_read的话，内容为空，因为前面已经使用了
        list_no = []  # 建立空白列表
        nut = linecache.getline('old_no.txt', 2)  # 读取文件的第二行并赋值给'nut'
        if nut == '':  # 如果'nut'的值为空白，则
            list_no.append(0)  # 给列表赋值“0”，这样就不会在后面eval函数转义时出错
            for line in file_read.readlines():  # 读取文件内容并且用reallines()函数生成列表形式
                list_no.append(list(map(int, line.split(','))))   # 将每行内容添加进列表，用'，'隔开，这样生成的列表里面每个字符都是子列表
            list_no_change = str(list_no).replace('[', '').replace(']', '').replace(' ', '')  # 用replace函数将子列表的"["&"]"&"空格"去掉，但是列表每个值还是字符串形式
            list_no_ok = list(eval(list_no_change))  # 应用强大的eval函数转义将字符串型转换成数据型，然后再将转义后的列表用list函数生成列表，再保存替换原来的列表中
            list_no_ok.sort()  # 列表按小到大排序
            del list_no_ok[0]  # 删除前面为了保护eval函数转义而添加的“0”
            set_no = set(list_no_ok)  # 将列表转换为集合，集合是无序的，所以下一行的输出不用集合，而用上一行排好序的列表
            print('之前保存的数据为:{}'.format(list_no_ok))  # 输出前面排好序的列表
            file_read.close()  # 文件打开了就必须要关闭-----------------------------自此，成功将文件内容读出并转换为int格式的集合-------------------------
        else:
            for line in file_read.readlines():  # 读取文件内容并且用reallines()函数生成列表形式
                list_no.append(list(map(int, line.split(','))))   # 将每行内容添加进列表，用'，'隔开，这样生成的列表里面每个字符都是子列表
            list_no_change = str(list_no).replace('[', '').replace(']', '').replace(' ', '')  # 用replace函数将子列表的"["&"]"&"空格"去掉，但是列表每个值还是字符串形式
            list_no_ok = list(eval(list_no_change))  # 应用强大的eval函数转义将字符串型转换成数据型，然后再将转义后的列表用list函数生成列表，再保存替换原来的列表中
            list_no_ok.sort()  # 列表按小到大排序
            set_no = set(list_no_ok)  # 将列表转换为集合，集合是无序的，所以下一行的输出不用集合，而用上一行排好序的列表
            print('之前保存的数据为:{}'.format(list_no_ok))  # 输出前面排好序的列表
            file_read.close()  # 文件打开了就必须要关闭-----------------------------自此，成功将文件内容读出并转换为int格式的集合-------------------------
    else:  # 判断文件内容为空，直接到输入起始数字位置开始
        pass

'''
    ------------------------------------------------在界面角落提供“重置”按钮，如果要清除之前的数据请按按钮-------------------------------------
print("确认要重置数据吗？是/否")#按下按钮后，弹出确认框，是对应True，否对应False，并赋值给reset_button按钮
if reset_button is True:
    file = open('old_no.txt', 'w')
    file.close()
else:
    if reset_button is False:
        pass
    -----------------------------------------------------------------以上为多行注释来屏蔽GUI界面的功能----------------------------------------
'''
'''
    ---------------------------------每次随机数据暂存内存，需要的话点击“保存”按钮写入到文件里，下次打开再点击读取---------------------------------
if save_button is True:
    list_set = list(set_no)  # 将集合转换成列表
    file = open('old_no.txt', 'w')  # 将数据处理后覆盖写入文件
    for i in range(len(list_set)):  # 用len()计算列表list_set的长度，并且历遍列表list_set
        s = str(list_set[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
else:
    if save_button is False:
        pass
    ----------------------------------------------------------------以上为多行注释来屏蔽GUI界面的功能-----------------------------------------
'''
# -----------------------------------------------将随机数的产生过程做成函数--------------------------------------------------


def ran_no(min_no_input, max_no_input):
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
        #  set_no.add(random_no)  # 随机数写入集合
    else:
        Random_Times = 1  # 定义函数用来计算随机次数
        while random_no in set_no:  # 判断随机数是否已存在，如果存在则重新产生随机数直到不存在
            print(str(random_no) + '：已经存在')  # 调试用的输出
            random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
            Random_Times = Random_Times + 1  # 每次循环次数加一
            Max_Random_Times = max_no**2  # 循环输入数值最大数的平方次数
            if Random_Times > Max_Random_Times:  # 当循环次数大于输入数值最大数的平方次数时
                break  # 退出循环，要求从新输入范围
        else:  # 经过循环重新产生不存在的随机数，然后写入集合
            print('新的随机数生成：' + str(random_no))  # 调试用的输出
            #  set_no.add(random_no)  # 随机数写入集合
    return random_no
# -----------------------------------------------将随机数的产生过程做成函数--------------------------------------------------


min_no_input = input('请输入想随机的起始数字:')  # 提示输入数据
max_no_input = input('请输入想随机的结尾数字:')
r_n = ran_no(min_no_input, max_no_input)  # 调用随机数函数并返回随机数然后赋值给r_n变量保存
set_no.add(r_n)  # 随机数写入集合

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
        set_no.add(random_no)  # 随机数写入集合
    --------------------------------------------------以上为多行注释来屏蔽GUI界面的功能---------------------------------------------
'''
# 以下编写将集合写入数据文件的代码
list_set = list(set_no)  # 将集合转换成列表
list_set.sort()  # 列表按小到大排序，这样输出到数据文件就是顺序的了

file = open('old_no.txt', 'w')
for i in range(len(list_set)):  # 用len()计算列表list_set的长度，并且历遍列表list_set
    s = str(list_set[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
    s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
    file.write(s)
file.close()
# -----------------------------------------------自此，成功将随机数写入数据文件--------------------------------------------------
