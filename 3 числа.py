a = int(input('введи а='))
b = int(input('введи b='))
c = int(input('введи c='))
if a < b > c:
    print(b)
if a < c > b:
    print(c)
if b < a > c:
    print(a)
print(max(a,b,c))
