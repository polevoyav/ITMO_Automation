# определяем функцию

def add(x, y):
    return x + y

# вызываем функцию
add(1, 2)

# определяем функцию
def add(x, y):
    return x + y

# вызываем фуккцию
print(add(1, 3))

# вызываем фуккцию
print(add('i a', 'm tester'))

def arg(a, b, c=2, d=3):
    return a + b + c + d

print(arg(1, 1, 1, 1))

print(arg(2, 2))

print(arg(2, 2, 10))

# print(arg(2, 2, '1', 1))    # текстовое значение в функции, ошибка


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d
print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='7'))

def arg1(a=(1,2,3,4)):
    return a[0]
print(arg1())
#
# def arg2(pi, r):
#     return pi * r ** 2
# print(arg2(3.14159, 3))

def arg2(a, pi=3.14259):
    return pi * a ** 2
print(arg2(3))

