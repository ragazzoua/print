# # def positive(lst):
# #     poslist = list(lst)
# #     i = 0
# #     while i < len(poslist):
# #         if lst[i] <= 0:
# #             del lst[i]
# #         i += 1
# #
# # lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
# # positive(lisn2)
# # print(lisn2)
#
# # def positive1(lst):
# #     for i in (list(lst)):
# #         if i > 0:
# #             print(i)
# #
# #
# #
# #
# # lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
# # positive(lisn2)
#
# def positive1(lst):
#
#     for i in (list(lst)):
#         if i > 0:
#             print(i)
#
#
#
#
# lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
# positive1(lisn2)
#
#
# def positive3(list1):
#     res = []
#     for i in range(len(list1)):
#         if list1[i] > 0:
#             res.append(list1[i])
#     return res
#
# lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
# print(positive3(lisn2))
#
#
# def replace(s, a, b):
#     list(s)
#     for i in range(0, len(s)):
#         if s[i] < 0:
#             s[i] = b
#     return s


def positive0(lst):
    for item in lst:
        if item <= 0:
            lst.remove(item)

lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
positive0(lisn2)
print(lisn2)

def positive(lst):
    for item in list(lst):
        if item <= 0:
            lst.remove(item)

lisn2 = [1, -2, 3, 4, 5, 6, 7, -9, -10, -8, 0]
positive(lisn2)
print(lisn2)