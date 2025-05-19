def sum_num(number):
  summ = 0
  max = 0
  min = 10
  while number > 0:
    digit = number % 10
    if digit > max:
      max =digit
    if digit < min:
      min = digit
    summ = summ + digit
    number = number // 10
  print("Сумма цифр равна ",summ,"большая цифра",max,"меньшая",min)

while True:
    number = int(input('Введите число: '))
    sum_num(number)
    break

