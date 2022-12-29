# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

print('Введите кол-во позиций для списка')
num = int(input())
print()

numbers = list()
k = 0
while num > k:
    rat = random.randint(0, 10)
    numbers.append(rat)
    k = k+1
print('Вид рандомного списка', numbers)
print()
# print('Введите рандомный список') // если хотим задать список через пользователя
# numbers = list((input()))
# print('Вид заданного списка', numbers)

def res(num):
    new_list = [num[0]]
    for i in range(1, len(num)):
        for j in range(len(new_list)):
            if new_list[j]==num[i]:
                break
            elif j == len(new_list)-1:
                new_list.append(num[i])
    print('Список неповторяющихся элементов исходной последовательности:')
    print(new_list)

res(numbers)