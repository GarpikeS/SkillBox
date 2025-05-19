#Напишите программу, которая получает на вход начало и конец отрезка, а также шаг (отрицательный), а затем высчитывает функцию y в каждой точке отрезка и выводит ответ на экран с нужным шагом, начиная с конца.
start = int(input("Введите начало отрезка:"))
finish = int(input("Введите конец отрезка:"))
step = int(input("Введите шаг:"))
gap = 0
x = 0
if start > finish and step > 0:
  gap = finish
  finish = start
  start = gap
  step = - step
for x in range(finish, start, step):
  print(x)
  y = x ** 3 + 2 * x ** 2 - 4 * x + 1
  print("y=",y,"при x=",x)
