#coding:UTF-8
random_no={1: 1, 2: 2.2, '3': 'three', '4': '4four'};#数值型的不用加引号，字符串型的键和值都要加引号
print(random_no[1])
print(type([random_no]))
print(str(random_no[1])+random_no['3'])
print(type([random_no[1]]))

#每次随机值生成字典键和值（两者相同，用in 操作符来判断是否存在，不在则写入；或者用 get()方法来判断，不在则顺便写入）
#字典函数资料：http://www.runoob.com/python3/python3-dictionary.html
#in 操作符：http://www.runoob.com/python3/python3-att-dictionary-in-html.html
#get()方法：http://www.runoob.com/python3/python3-att-dictionary-get.html