import math

a = float(input('Початкове значення a:'))
b = float(input('Кінцеве значення b:'))
h = float(input('Розмір кроку h:'))

#всі значення аргументу і функції
spisok1 = []
#добутки елементів кожного рядка
spisok2 = []

x = a
while x <= b:
    y = abs(math.tan(abs(x) + 0.1))
    spisok1.append("x=%.1f y=%.3f" %(x, y))
    spisok2.append(x * y)
    x=x+h

for el in spisok1:
    print([el])

print(spisok2)