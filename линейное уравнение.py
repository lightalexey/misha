# решение линейного уравнения вида ax + b = 0
a = int(input('введи а ='))
b = int(input('введи б ='))
if a != 0:
    x = -b/a
    print(x)
else:
    if b == 0:
        print('любое число')
    else:
        print('нет корней')
