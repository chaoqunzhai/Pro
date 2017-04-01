def Counter(Index, Start, End):
    print("第%d次计算，第一个数字是%d，第二个数字是%d" % (Index, Start, End))
    if Index == 10:  # 如果要计算的值是10就退出
        return Start
    N = Start + End  # N等于第一个数加上第二个数
    Number = Counter(Index + 1, End, N)  # 继续调用计数器函数，End相当与传给函数的第一个数，N是传给函数的第二个数
    return Number
result = Counter(1, 0, 1)
print("得出的数字是：", result)