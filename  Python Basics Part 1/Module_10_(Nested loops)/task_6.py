#Напишите программу, которая выводит на экран равнобедренный треугольник (пирамидку), заполненный символами хештега (#). Пусть высоту пирамиды определяет пользователь.
size = int(input("Введите высоту пирамиды:"))
bill = (2 * size) - 2
for check in range(0, size):
    for perem in range(0, bill):
        print(end=" ")
    bill -= 1
    for score in range(0, check + 1):
        print("#", end=' ')
    print(" ")