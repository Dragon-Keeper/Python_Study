def invest():
    amount1 = input("初始金额:")
    amount = int(amount1)
    rate1 = input("年利率:")
    rate = float(rate1)
    times1 = input("时长:")
    times = int(times1)
    for time in range(1, times):
        amount = amount * (1 + rate)
        print('第{}年: $'.format(time) + str(amount))
    invest()


invest()
