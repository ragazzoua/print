# def isInList(e, lst):
#     if e in lst:
#         return lst.count(e)
#     else:
#         return 0
#
#
# lst = [0, 2, 1, 3]
# print(isInList(0, lst))
#
#
# def count(e, lst):
#     if e in lst:
#         return lst.count(e)
#     else:
#         return 0


# def replace1(oldList, a, b):
#     newList = list(oldList)
#     for i in oldList:
#         if oldList[i] == a:
#             newList[i] = b
#         return newList
#
#
# list1 = [1, 2, 3, 4, 5]
# replace1(list1, 5, 3)
# print(list1)


# def replace1(s, a, b):
#     list(s)
#     for i in range(0, len(s)):
#         if s[i] == a:
#             s[i] = b
#     return s
#
#
# list1 = [1, 2, 3, 4, 5]
# print(replace1(list1, 5, 0))


# def exclude(lst1, lst2):
#     for i in lst2:
#         if i in lst1:
#             lst1.remove(i)
#     return lst1
#
#
# list3 = [1, 2, 0, 4, 5]
# list4 = [1, 2, 3, 4, 6]
#
# print(exclude(list3, list4))

def myzip(list0, list1):
    res = []
    if len(list0) == len(list1):
        for i in range(len(list0)):
            res.append([list0[i], list1[i]])
        return res
    else:
        print("You must provide the same length list")


# def myzip1(l1, l2):
#     res = []
#     i = 0
#     while i < len(l1):
#         res += [[l1[i], l2[i]]]
#         i += 1
#     return res


list3 = [1, 2, 4, 6]
list4 = [9, 2, 3, 4, 6]

print(myzip(list3, list4))

# def replace(s, a, b):
#     i = 0
#     newList = list(s)
#     while i < len(s):
#         if s[i] == a:
#             newList[i] = b
#         i += 1
#     return newList
