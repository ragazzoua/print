b = [[1, 2, 3], [4, 5, 6]]


def flatten(lst):
    res = []
    for i in lst:
        for j in i:
            res.append(j)
    return res


print(flatten(b))
