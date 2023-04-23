print('первое задание')


a = 50
b = -100
def ab(a, b):
    return (a > b)
print('наибольшее из чисел:')
if ab(a, b):
    print(a)
else:
    print(b)
print()
print('второе задание')

a = 5
b = 141
def ab(a, b):
    return ((a == 135 + b) or (b == 135 + a))
print('Отличаются на 135:')
if ab(a, b):
    print('YES')
else:
    print('NO')
print()

print('третье задание')

mes = 23
if mes == 1 or mes == 2 or mes == 12:
    print('зима')
elif mes == 3 or mes == 4 or mes == 5:
    print('весна')
elif mes == 6 or a == 7 or mes == 8:
    print('лето')
elif mes == 9 or mes == 10 or mes == 11:
    print('осень')
else:
    print('такого месяца не существует')
print()

print('четвертое задание')
a = 13
b = 12
c = 22
if a > 10 and b > 1 and c > 10:
    print('YES')
else:
    print('NO')
print()

print('шестое задание')
def chdn(god, mes):
    return god * 12 * 29 + mes * 29
print(chdn(0,1))
print()
