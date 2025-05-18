number = int(input("Введите число:"))
check = 1
factorial = 1
for check in range(1,number+1):
  factorial = factorial * check
print("Факториал числа",number,"равен",factorial)
