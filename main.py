# #Первое задание: нужно найти простое число
# num = int(input())
# if num <= 1:
#    print('Число не простое')
# else:
#    for i in range(2, num):
#        if num % i == 0:
#           print('Число не простое')
#           break
#    else:
#        print('Число просто')

# Второе задание: найти по возрастанию
mas = [3456,235678,2677,-235,23,178,0]
for i in range(len(mas)):
    for x in range(i + 1, len(mas)):
        if mas[i] > mas[x]:
           mas[i], mas[x] = mas[x], mas[i]
print(mas)

#Третье задание: найти наибольшее число в массиве
# mas = [1,6,3,2,5,6,2,3,56,5,4,3,3,45,3,2,2,1,2,3,4,57,9,0,9,87,543,4, -3, -333]
# maximum = mas[0]
# for i in mas:
#     if i > maximum:
#         maximum = i
# print(maximum)

# Четвертое задание: фибоначчи
# fib = int(input())
# a = 1
# b = 1
# print(a, b, end=' ')
# for i in range(2, fib):
#    a,b = b, a + b
#    print(b, end=' ')