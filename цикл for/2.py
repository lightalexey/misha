k1 = 0 
a = int(input('введи а='))
for i in range(1,a + 1):
    if a % i == 0:
        print(i) 
        k1 += 1
print('количество делителей', k1)       
