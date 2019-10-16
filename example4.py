def xsum(n):
    symbol = 1
    res = 0
    for i in range(1, n + 1):
        res = res + i * symbol
        symbol = symbol * (-1)
    return res


print(xsum(5))
