def print_sequence(from_=0, to=10, step=1):
    for x in range(from_, to, step):
        print(x)


print_sequence(from_=1, step=1)


def f(p):
    v = 10
    return v * g * p


g = 100
print(f(1), g)


x = list("abc")
print(x)
print(x.__getitem__(1))