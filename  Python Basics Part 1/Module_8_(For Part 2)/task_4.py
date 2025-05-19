#Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.
start = int(input("Введите начало отрезка:"))
finish = int(input("Введите конец отрезка:"))
devider = int(input("Введите делитель:"))
check = 0
summ = 0
quantity = 0
for check in range(start,finish+1):
  if check%devider == 0:
    summ = summ + check
    quantity = quantity + 1
average = summ/quantity
print("Среднее арифметическое",devider,"равна:",average)