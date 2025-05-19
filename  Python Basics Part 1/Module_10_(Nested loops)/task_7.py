#Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами:
level = int(input('Введите количество уровней пирамиды: '))
number = 1

for row in range(1, level+1):
  print('\t' * (level - row), end = '')
  for col in range(row):
    print(number, end = '')
    number += 2
    print('\t' * 2, end = '')
  print()