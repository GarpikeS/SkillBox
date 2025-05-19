first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

print('Наибольшее число:',
      (first_number // second_number * first_number + second_number // first_number * second_number) // (
                  first_number // second_number + second_number // first_number))