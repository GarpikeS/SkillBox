N = int(input("Введите число N:"))
check = 0
summ = 0
for check in range(N):
  elem = ((-1) ** check) * (1 / (2 ** check))
  summ = summ + elem
print("Сумма элементов числа N = ",summ)