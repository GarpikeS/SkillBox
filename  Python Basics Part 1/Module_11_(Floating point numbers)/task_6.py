x1, y1 = float(input('Введите местоположение коня: \n')), float(input())
x2, y2 = float(input('Введите местоположение точки на доске: \n')), float(input())
if (int(10 * x1) - int(10 * x2)) * (int(10 * y1) - int(10 * y2)) in range(-2,2):
  print('Да')
else:
  print('Нет')