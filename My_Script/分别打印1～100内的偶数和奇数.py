num_list = []
for num2 in range(1, 101):
    if num2 % 2 == 0:  # 通过整除‘%’来筛选出偶数
        print(num2)
    else:
        num_list.append(num2)  # 筛选出奇数存入列表
print('---------------------------------------------------')
for num1 in num_list:
    print(num1)
