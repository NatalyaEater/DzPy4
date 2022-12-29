# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов


with open("text.txt","r") as file:
    data1 = file.read()
with open("text2.txt","r") as file:
    data2 = file.read()

st = data1.split(" = ")
result = st[0] + " + " + data2

with open("task5res.txt", "w") as file2:
    file2.write(result)