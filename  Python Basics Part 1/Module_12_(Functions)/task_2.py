def test():
  number = int(input("Введите число: "))
  if number > 0:
    positive()
  elif number == 0:
    zero()
  else:
    negative()
def positive():
  print("Положительное")
def negative():
  print("Отрицательное")
def zero():
  print("0")

test()
