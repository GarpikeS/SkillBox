cord_x = 8
cord_y = 10
command = input('Марсоход находится на позиции 8, 10 введите команду: ')
while cord_x != -1 and cord_y != -1:
  if cord_x < 15 and cord_y <20:
    if (command == 'W') or (command == 'w'):
      cord_y += 1
      print('Марсоход находится на позиции', cord_x, cord_y,'введите команду: ')
      command = input()
    elif (command == 'S') or (command == 's'):
      cord_y -= 1
      print('Марсоход находится на позиции', cord_x, cord_y,'введите команду: ')
      command = input()
    elif (command == 'A') or (command == 'a'):
      cord_x -= 1
      print('Марсоход находится на позиции', cord_x, cord_y,'введите команду: ')
      command = input()
    elif (command == 'D') or (command == 'd'):
      cord_x += 1
      print('Марсоход находится на позиции', cord_x, cord_y,'введите команду: ')
      command = input()