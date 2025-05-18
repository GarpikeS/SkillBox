#Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
first_number = int(input("Введите первое число:"))
second_number = int(input("Введите второе число:"))
check = 0
summ = 0
quantity = 0
average = 0
for check in range(first_number, second_number):
  if check%3 == 0:
    summ = summ + check
    quantity = quantity + 1
average = summ/quantity
print("Среднее арифметическое:",average)