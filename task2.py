# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('Введите число')
num = int(input())
print()


def list_N(N):
    j = []
    i = 2
    while N > 1:
        if N % i == 0:
            j.append(i)
            N = N // i
        else:
            i = i+1
    return j


print(list_N(num))
