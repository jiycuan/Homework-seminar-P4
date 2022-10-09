# 1. Вычислить число π c заданной точностью d

d = float(input('Укажите число в формате "0.001", опционально меняя количество нулей. Единица отсекает до какой точки число π должно быть посчитано верно: '))

enjoy = 0
divisor = 1
factor = 1
leibniz_cur = 1

def leibniz(a, b):
    return b * 4 / a

while abs(leibniz_cur) > d / 10:
    leibniz_cur = leibniz(divisor, factor)
    enjoy = enjoy + leibniz_cur
    divisor = divisor + 2
    factor = -1 * factor

print(enjoy)
   

#. 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Укажите число N:'))
bill = []
count = 2

while N > 1:
    if N % count == 0:
        bill.append(count)
        N = N / count
    else:
        count = count + 1

print(bill)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

bill = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
sort = []
dup = {x for x in bill if bill.count(x) > 1}

for i in range(len(bill)):
    if bill[i] not in sort and bill[i] not in dup:
        sort.append(bill[i])

print(sort)

# 4. Дана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


import random
k = int(input('Укажите степень k:'))
list_of_factor = []
poly = str('X')
holy = []
enjoy = str
j = k

for i in range(k):
    list_of_factor.append(int(random.randrange(1, 101)))

for i in range(j):
    if i == k - 1:
        enjoy = str(list_of_factor[i]) + poly
        holy.append(enjoy)
    else:
        enjoy = str(list_of_factor[i]) + poly + ('^') + str(j)
        holy.append(enjoy)
    j = j - 1
    

result = str(holy[0]) + ' + '

for i in range(1, k):
    if i == k - 1:
        result = str(result) + str(holy[i]) + str(' = 0 ')
    else:
        result = str(result) + str(holy[i]) + str(' + ')

print(result)

my_file = open("4_k_result.txt", "a+")
my_file.write(result)
my_file.close()

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

with open("5_one.txt", "r") as file:
    poly_1 = file.read()
with open("5_one_too.txt", "r") as file:
    poly_2 = file.read()

poly_1 = str.replace(poly_1, "- ", "+ -").split()
poly_2 = str.replace(poly_2, "- ", "+ -").split()

poly_1 = list(filter(lambda x: x != "+" and x != "=" and x != "0", poly_1))

print(poly_1)

my_file = open("5_result.txt", "w+")
my_file.write(poly_1)
my_file.close()