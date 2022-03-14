a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + D ** (1 / 2)) / 2 / a
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    print('x1=', x1)
    print('x2=', x2)
elif D < 0:
    print('действительных корней нет')
else:
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    print('x1=x2=', x1)
