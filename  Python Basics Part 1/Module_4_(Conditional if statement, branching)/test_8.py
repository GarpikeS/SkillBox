print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно
first_number = int(input("Введите первое число:"))
second_number = int(input("Введите второе число:"))
thiird_number = int(input("Введите третье число:"))
if first_number > second_number:
  if first_number > thiird_number:
    print("Наибольшее число=", first_number)
  else:
    print("Наибольшее число=", thiird_number)
else:
  if second_number > thiird_number:
    print("Наибольшее число=", second_number)
  else:
    print("Наибольшее число=", thiird_number)