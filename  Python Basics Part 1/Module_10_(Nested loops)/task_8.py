#Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:
level = int(input('Введите число: '))
width = level * 2
for coln in range (1, level+1):
  print_num = level
  for row in range (width):
    if row < coln:
      print (print_num, end = '')
      print_num -= 1
    elif row > width - 1 - coln:
      print_num += 1
      print (print_num, end = '')
    else:
      print ('.', end = '')
  print ()