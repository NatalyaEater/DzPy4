# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import Decimal

print('Задайте точность рандомного вычисления формате 0.0001:')
num3 = float(input())

print('Для примера будем использовать умножение двух чисел.')

print('Введите первое число')
num1 = float(input())
print('Введите второе число')
num2 = float(input())

res =num1*num2

def num_d(num, d):
    number = Decimal(num)
    return number.quantize(Decimal(f"{d}"))

print(num_d(res,num3))