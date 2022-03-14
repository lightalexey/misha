a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a + b > c and a + c > b and b + c > a:
    # print('треугольник можно построить')
    if a == b == c:
        print('равносторонний треугольник')
    else:
        if a == b or b == c or a == c:
            print('равнобедренный треугольник')
        else:
            if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
                print('прямоуг треугольник')
            else:
                print('произвольный треугольник')
else:
    print('нельзя построить треугольник')
