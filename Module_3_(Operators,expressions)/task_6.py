first_number = int(input('Введите пожалуйста первое число:'))
second_number = int(input('Введите пожалуйста второе число:'))

ranks_first = first_number//100
print(ranks_first)
ranks_second = second_number//100
print(ranks_second)

last_two_number_first = first_number % ranks_first
last_two_number_second = second_number % ranks_second
print(last_two_number_first)
print(last_two_number_second)

result = last_two_number_first + last_two_number_second
print("Сумма:",result