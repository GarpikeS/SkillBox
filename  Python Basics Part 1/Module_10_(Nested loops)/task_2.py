N = int(input("Введите число:"))
check = 1
for line in range(N+1):
  for column in range(line):
    print(line, end = " ")
  print(' ')
