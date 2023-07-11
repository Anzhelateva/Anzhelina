a = 5
b = 6
c = 7

# вычисляем полупериметр
p = (a + b + c) / 2
# вычисляем площадь
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

# `round(num, count)` используется для округления числа в ближайшую сторону
# `count` - количество цифр после запятой
print(f'Площадь треугольника со сторонами {a}, {b} и {c} равняется {round(s, 2)}')
