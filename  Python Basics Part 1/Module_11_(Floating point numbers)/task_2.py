import math

n = int(input('Введите кол-во чисел: '))
for i in range(n):
  number = float(input('Введите число: '))
  if (number > 0):
     print('x =', math.ceil(number),'log(x) = ', math.log(math.ceil(number)))
  elif (number < 0):
     print('x =', math.floor(number),'log(x) = ', math.exp(math.floor(number)))
  else:
     print('0')
