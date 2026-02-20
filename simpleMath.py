# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# tut schitajem ploshczad kruga
valuePi = 3.14
radiusCircle = 5
areaCircle = valuePi * (radiusCircle**2)
print("Дано: число Pi = ", valuePi)
print("      Радиус круга = ", radiusCircle)
print("Площадь круга: ", areaCircle)
# tut schitajem dlinu okruznosti
circumference = 2 * valuePi * radiusCircle
print("Длина окружности: ", round(circumference, 2)) #используем функцию раунд, потому что питон хранит числа в двоичном коде, а 3.14 это бесконечная дробь
# Посчитаем площадь прямоугольника 
sideA = valuePi
sideB = radiusCircle
areaRectangle = sideA * sideB
#длинная строка чисто для красоты вывода
print("Площадь прямоугольника со сторонами", sideA, "и", sideB, "=", round(areaRectangle, 2))

