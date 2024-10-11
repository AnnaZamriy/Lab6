import math

a = float(input('Початкове значення a:'))
b = float(input('Кінцеве значення b:'))
h = float(input('Розмір кроку h:'))

n = int((b - a) / h) + 1
for i in range(n):
    x = a + i * h
    y = abs(math.tan(abs(x) + 0.1))
    print("%i x=%.1f y=%.3f"%(i,x,y))