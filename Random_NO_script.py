# coding: UTF-8
import random  # 导入随机函数random模块，这样下面才能使用random函数产生随机数

set_no = set()  # 生成空白集合，否则后面生成的随机数无法合法写入集合，因为集合还没有被定义
list_set = []  # 建立空白列表
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
        print('新的随机数生成：' + '\033[0;37;42m\t{}\033[0m'.format(str(random_no)))  # 调试用的输出
        #  set_no.add(random_no)  # 随机数写入集合
    else:
        Random_Times = 1
        while random_no in set_no:  # 判断随机数是否已存在，如果存在则重新产生随机数直到不存在
            print(str(random_no) + '：已经存在')  # 调试用的输出
            random_no = random.randint(min_no, max_no)  # 产生范围内的随机数
            Random_Times = Random_Times + 1
            Max_Random_Times = max_no**2
            if Random_Times > Max_Random_Times:
                break
        else:  # 经过循环重新产生不存在的随机数，然后写入集合
            print('新的随机数生成：' + '\033[0;37;42m\t{}\033[0m'.format(str(random_no)))  # 调试用的输出
            #  set_no.add(random_no)  # 随机数写入集合
    return random_no
# -----------------------------------------------将随机数的产生过程做成函数--------------------------------------------------


min_no_input = input('请输入想随机的起始数字:')  # 用正则表达式提示输入数据
max_no_input = input('请输入想随机的结尾数字:')

count = 1
while count < round(float(max_no_input))**2:
    print('之前保存的数据为:{}'.format(list_set))  # 输出前面排好序的列表
    r_n = ran_no(min_no_input, max_no_input)  # 调用随机数函数并返回随机数然后赋值给r_n变量保存
    set_no.add(r_n)  # 随机数写入集合
    list_set = list(set_no)  # 将集合转换成列表
    list_set.sort()  # 列表按小到大排序，这样输出到数据文件就是顺序的了
    print('最新的数据为：{}'.format(list_set))  # 输出前面排好序的列表
    detect = input('如果输入单词“c”则程序继续执行，否则退出程序:')  # 通过输入字符来判断是否继续产生随机数还是退出
    if detect == 'c':
        count = count + 1
    else:
        break
