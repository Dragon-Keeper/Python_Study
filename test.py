# coding:UTF-8
list = ["a", "b,", "c", "d", "f", "f", "g", "h,", "i"]  # 写一个列表
if "f" in list:  # 判断是否存在一个元素
    cnt = list.count("f")
    print(type(cnt))
    print(str(cnt) + '个f')
    print("{0}个f".format(cnt))
