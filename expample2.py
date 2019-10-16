# sum = 1
# n = 5
#
# for i in range(1, n+1, 2):
#     sum *= i
# print(sum)

# n = 5
# prod = 1
# for i in range(1, n + 1, 2):
#     prod *= i
# print(prod)
#
# n = 5
# i = 0
# sum = 0
# base= 2
# while i <= n:
#     sum = sum + base ** i
#     i += 1
# print(sum)

# n = 4
# c = 0
# while a > 0:
#     if n % a == 0:
#         c += 1
#     a -= 1
# print(c)

# m = 10
# sum = 0
# i = 1
# while (m % i == 0):
#     sum = sum + i
#     i += 1
# print(sum)


m= 10
d = 0
i = 1
while i <= m:
    if m % i == 0:
        d = d + i
    i += 1
print(d)
