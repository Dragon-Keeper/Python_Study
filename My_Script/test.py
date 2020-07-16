# coding: UTF-8
import numpy
import random

set_no = set()  # 生成空白集合，否则后面生成的随机数无法合法写入集合，因为集合还没有被定义
list_set = []  # 建立空白列表
res_lis = []  # 储存序号数组转成的列表
res_out = []  # 储存函数随机结果的列表
res_lis_all_in_one = []  # 存放所有序号的列表
ran_out = []

no_input = input('请输入想随机的数序:')  # 用正则表达式提示输入数据


def ra_no(no_input):
    no = round(float(no_input))  # 由于input函数输入的是str字符串型，必须转换为整数型才能进行随机运算，直接用int转换的话提示错误，所以先用float转换为浮点型，然后再用round取整去小数点
    # -----------------------------以上为获取输入数序--------------------------------

    l_set = [int(item) for item in str(no)]
    # print('输入的数字生成列表：', l_set)  # 调试输入是否生成列表
    # ----------------------------以上将输入数序拆开成列表---------------------------

    i = 0  # 用于计算次数，控制列数与输入数字相加的次数
    c = 10  # 用于与输入数字相加的基础

    # ran_no_lis = []  # 随机结果列表
    for x in l_set:  # 依次提取列表内的数值
        print('依次提取输入的数字：', x)  # 调试显示每次从列表内提取的数值
        k = [i + 1 for i in range(x)]  # 将从列表提取出的数值迭代
        ar = numpy.array(k)  # 为下一步整数加列表做列表转换数组
        result = c + ar  # 将列数加上座位顺序得到那列的序号
        # print('依次提取输入的数字并加10：', result)  # 调试结果生成数组
        res_lis.append(result.tolist())  # 结果生成的数组转列表
        # print('显示结果合集：', res_lis)  # 调试生成的数组转列表结果
        c = c + 10  # 每完成一列就加10到第二列
        i = i + 1
    res_lis_all_in_one = [y for x in res_lis for y in x]  # 将嵌套的列表合一
    # print("嵌套的列表合一结果：", res_lis_all_in_one)  # 调试嵌套的列表合一结果
    # -----------------------------以上将生成的列表合成一个全体列表--------------------

    # ran_no = random.choice(res_lis_all_in_one)  # 随机出一个列表内的数值
    # print("随机结果：", ran_no)  # 调试从列表随机出一个数值的结果
    # -----------------------------以上从全体列表里随机出一个数字----------------------

    # res_lis_all_in_one.remove(ran_no)  # 从全体列表里清除刚刚随机出来的结果
    # print("随机后的全体列表：", res_lis_all_in_one)  # 调试显示随机后的全体列表
    # 第一种做法--------------------从全体列表里随机出一个数字后，并从全体列表里删除掉这个数字，下次随机从剩下数值里随机产生

    # while ran_no in ran_no_lis:
    #    ran_no = random.choice(res_lis_all_in_one)  # 随机出一个列表内的数值
    #    print("再次随机出的结果：", ran_no)  # 调试从列表随机出一个数值的结果
    #    ran_no_lis.append(ran_no)  # 将随机结果存入随机结果列表中
    #    print("再次随机出的结果添加入随机结果列表：", ran_no_lis)  # 调试显示随机结果列表
    # 第二种做法--------------------从全体列表里随机出一个数字后，并与“随机结果列表”比对，不在“随机结果列表”里的话就存入并输出，已存在的话重新随机
    # 第二种做法虽然太复杂了，但第一种方法在函数内每次随机都会重新生成列表，无法再次删除已随机数值

    return res_lis_all_in_one
    # -----------------------------将随机数的产生过程做成函数---------------------


res_out = ra_no(no_input)  # 通过函数获取座位结果列表，这句必须在while循环外，否则重复生成座位结果列表
count = 1
while count < int(no_input):
    # print("随机结果列表：", res_out)  # 调试随机结果列表的输出
    ran_no = random.choice(res_out)  # 随机出一个列表内的数值
    while ran_no in ran_out:  # 如果随机存在结果列表内，再在座位结果列表里随机出另一个
        ran_no = random.choice(res_out)  # 随机出一个列表内的数值
        print("再次随机出的结果：", ran_no)  # 调试从列表随机出一个数值的结果
        # -------------------------下面加入退出循环判断，如果随机出全部数据则退出随机循环
        count = count + 1
        Max_Random_Times = int(no_input)
        if count > Max_Random_Times:
            break
    else:
        print("随机结果：", ran_no)  # 调试从列表随机出一个数值的结果
        ran_out.append(ran_no)  # 将随机结果存入随机结果列表中
        # print("随机结果添加入随机结果列表：", ran_out)  # 调试显示随机结果列表
# -----------------------------以上获取座位结果列表并随机出一个座位并存入随机结果列表
    detect = input('如果输入数字“0”则程序继续执行，否则退出程序:')  # 通过输入字符来判断是否继续产生随机数还是退出
    if (int(detect)) == 0:
        continue
    else:
        break
