import math
R = float(input('Введите радиус планеты: '))
V = 10.8321 * (10 ** 11)
V1 = round(4 * math.pi/3 * (R**3), 3)
if V1 < V:
    print('Объём планеты Земля больше в', round(V/V1, 3), 'раз')
else:
    print('Объём планеты Земля меньше в', round(V1/V, 3), 'раз')