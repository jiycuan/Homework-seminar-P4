# 1. Вычислить число π c заданной точностью d

d = float(input('Укажите число в формате "0.001", опционально меняя количество нулей. Единица отсекает до какой точки число π должно быть посчитано верно: '))

temp = 0
divisor = 1
factor = 1
leibniz_cur = 1

def leibniz(a, b):
    return b * 4 / a

while abs(leibniz_cur) > d / 10:
    leibniz_cur = leibniz(divisor, factor)
    temp = temp + leibniz_cur
    divisor = divisor + 2
    factor = -1 * factor

print(temp)
   

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
temp = str
j = k

for i in range(k):
    list_of_factor.append(int(random.randrange(1, 101)))

for i in range(j):
    if i == k - 1:
        temp = str(list_of_factor[i]) + poly
        holy.append(temp)
    else:
        temp = str(list_of_factor[i]) + poly + ('^') + str(j)
        holy.append(temp)
    j = j - 1
    

result = str(holy[0]) + ' + '

for i in range(1, k):
    if i == k - 1:
        result = str(result) + str(holy[i]) + str(' + ') + str(random.randrange(1, 101)) + str(' = 0 ')
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

poly_1 = poly_1.split()
poly_2 = poly_2.split()

poly_temp = []
poly_temp_exmax = []

if len(poly_1) > len(poly_2):
    poly_max = poly_1
    poly_min = poly_2
    temp = len(poly_1) - len(poly_2)
    for i in range(temp - 1):
        poly_temp.append(poly_1[i])
    for i in range(len(poly_1) + 1 - temp):
        poly_temp_exmax.append(poly_1[i + temp - 1])   
else:
    poly_max = poly_2
    poly_min = poly_1
    temp = len(poly_2) - len(poly_1)
    for i in range(temp - 1):
        poly_temp.append(poly_2[i])
    for i in range(len(poly_2) + 1 - temp):
        poly_temp_exmax.append(poly_2[i + temp - 1])

poly_min = (" ".join(poly_min))
poly_temp_exmax = (" ".join(poly_temp_exmax))

def poly_cortege(poly_string):
    poly_string = str.replace(poly_string, "- ", "+ -").split()
    poly_string = list(filter(lambda x: x != "+" and x != "=" and x != "0", poly_string))
    for i in range(len(poly_string)):
        poly_string[i] = poly_string[i].split("*")
    return poly_string

poly_min = poly_cortege(poly_min)
poly_temp_exmax = poly_cortege(poly_temp_exmax)

poly_result = []

for i in range(len(poly_min)):
    poly_result.append(int(poly_min[i][0]) + int(poly_temp_exmax[i][0]))
    poly_temp_exmax[i][0] = str(poly_result[i])

for i in range(len(poly_temp_exmax)):
    if i == len(poly_temp_exmax) - 1:
        poly_result[i] = str(poly_temp_exmax[i][0]) + " = 0"
    else:
        poly_result[i] = str(poly_temp_exmax[i][0]) + "*" + str(poly_temp_exmax[i][1]) + " +"

poly_result = (" ".join(map(str,poly_result)))
poly_result = str.replace(poly_result, "-", "- ")
poly_temp = (" ".join(map(str,poly_temp))) + " "

poly_result = poly_temp + poly_result
print(poly_result)

my_file = open("5_result.txt", "a+")
my_file.write(poly_result)
my_file.close()