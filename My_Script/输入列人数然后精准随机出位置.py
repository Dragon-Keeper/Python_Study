'''
一个输入框，按顺序输入每列人数，然后按照数字位数得到列数a，
之前的输入分解得到每列的人数b，然后根据a和b可以生成“数组”的数据c，
再在c里面随机出结果。
例：按顺序输入5列人数：67767，分别对应12345列，则每列学生对应为11-16、21-27、31-37、
41-46、51-57。在这些数里随机出结果就行。
'''
# coding: UTF-8
import random  # 导入随机函数random模块，这样下面才能使用random函数产生随机数

set_no = set()  # 生成空白集合，否则后面生成的随机数无法合法写入集合，因为集合还没有被定义
list_set = []  # 建立空白列表
# -------------------------------将随机数的产生过程做成函数-----------------------


def ran_no(no_input):
    no = round(float(no_input))  # 由于input函数输入的是str字符串型，必须转换为整数型才能进行随机运算，直接用int转换的话提示错误，所以先用float转换为浮点型，然后再用round取整去小数点
# --------------------------------以上为获取输入数序-----------------------------
    l_set = [int(item) for item in str(no)]
    # print(list_set) # 调试输入是否生成列表
# --------------------------------以上将输入数序拆开成列表------------------------
    l_no = len(l_set) + 1  # 获取列表长度用于拆分列表
    print(l_no)  # 调试列表长度是否生成列表
# --------------------------------以上将拆开的列表生成对应的列表-------------------


# --------------------------------以上将生成的列表合成一个全体列表-----------------


# --------------------------------从全体列表里随机出一个数字，并与“存在集合”比对，不在“存在集合”里的话就存入并输出，已存在的话重新随机
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


no_input = input('请输入想随机的数序:')  # 用正则表达式提示输入数据

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
