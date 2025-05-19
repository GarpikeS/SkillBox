number = float(input("Введите число:"))
check = 0
if number < 1:
  while number < 1:
    number *= 10
    check -= 1
elif number >= 10:
  while number >= 10:
    number /= 10
    check += 1
print("Формат плавающей точки: x =",number, "* 10 **",check)