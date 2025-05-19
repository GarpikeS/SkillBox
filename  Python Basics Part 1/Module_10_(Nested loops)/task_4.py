# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.
count = 0
quantity = int(input("Введите колличество чисел:"))
for check in range(quantity):
    number = int(input("Введите число:"))
    for score in range(number):
        test = True
        k = number - 1
        while k > 1:
            if number % k == 0:
                test = False
                break
            k -= 1
        if test:
            print(number)
            count += 1
            break
print("Простых чисел:", count)




