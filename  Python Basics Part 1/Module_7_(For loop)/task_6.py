#Напишите программу, которая находит и выводит все двузначные числа, равные утроенному произведению своих цифр. К таким относятся, например, 15 и 24.
check = 0
first_rank = 0
second_rank = 0
for check in range(10,100):
  if check%10 != 0:
   second_rank = check//10
   first_rank = check - second_rank * 10
   if check%(3 * first_rank * second_rank) == 0:
     print(check)