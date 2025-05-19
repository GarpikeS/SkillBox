def counting_digits(num):
    count_ = 0
    while num > 0:
        count_ += 1
        num //= 10
    return count_


def permul(num):
    temp = num
    n = 1
    last = num % 10
    temp //= 10
    while temp:
        first = temp % 10
        temp //= 10
        n *= 10
    middle = num % (first * n) // 10
    return last * n + middle * 10 + first


f = 1
while True:
    if f == 1:
        num_1 = int(input("Введите первое число: "))
        if counting_digits(num_1) < 3:
            print("В первом числе меньше трёх цифр.")
            continue
    f = 2
    num_2 = int(input("Введите второе число:"))
    if counting_digits(num_2) > 3:
        print("Числа до изменения\n")
        print("Первое число  - ", num_1, "\nВторое - ", num_2, "\n")
        num_1, num_2 = (permul(num_1), permul(num_2))
        print("Числа после изменения\n")
        print("Число 1 -", num_1, "\nчисло 2 -", num_2, "\n")
        print("Сумма:", sum((num_1, num_2)))
        break
    print("Во втором числе меньше четырёх цифр.")
