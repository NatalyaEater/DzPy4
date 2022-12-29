# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

print('Введите степень k')
num = int(input())
print()

i = num
res = ''
while i > -1:
    if (i == num):
        a = randint(1, 100)
        if a == 1:
           res = 'x^' + str(i) 
        res = str(a) + '*x^' + str(i)
    elif i > 1:
        a = randint(0, 100)
        if a == 1:
            res = res + ' + x^' + str(i)
        elif a > 1:
            res = res + ' + ' + str(a) + '*x^' + str(i)
    elif i == 1:
        a = randint(0, 100)
        if a > 1:
            res = res + ' + ' + str(a) + '*x'
        elif a == 1:
            res = res + ' + x'
    else:
        a = randint(0, 100)
        if a > 1:
            res = res + ' + ' + str(a) + ' = 0'
        else: res = res + ' = 0'
    i = i - 1
data = open('text.txt', 'a')
data.write(res)
data.close()