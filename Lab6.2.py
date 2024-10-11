import math

a = float(input('Початкове значення a:'))
b = float(input('Кінцеве значення b:'))
h = float(input('Розмір кроку h:'))

x = a
while x <= b:
    y = abs(math.tan(abs(x) + 0.1))
    print("x=%.1f y=%.3f"%(x,y))
    x=x+h