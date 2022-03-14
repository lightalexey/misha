a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a + b > c:
   if b + c > a :
       if a+c>b:
         print('можно построить треугольник')
       else:
            print('нельзя построить треугольник')
   else:
        print('нельзя построить треугольник')
else:
    print('нельзя построить треугольник')