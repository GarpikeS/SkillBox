def count_letter():
  text = input('Введите текст: ')
  number = int(input('Какую цифру ищем? '))
  letter = input('Какую букву ищём? ')
  number_count, letter_count = 0, 0

  for symbol in text:
    if symbol == letter:
      letter_count += 1
    elif symbol == str(number):
      number_count += 1
  print('\nКоличество цифр', number, '-', number_count)
  print('Количество букв', letter, '-', letter_count)

count_letter()