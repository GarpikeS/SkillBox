def reverse(n):
    result = 0
    while n > 0:
        n, r = divmod(n, 10)
        result = 10 * result + r
    return result


n = int(input("Введите первое число:"))
first_number = reverse(n)
print("Первое число наоборот:", first_number)
n = int(input("Введите второе число:"))
second_number = reverse(n)
print("Второе число наоборот:", second_number)
summ = first_number + second_number
print("Сумма:", summ)
reverse_summ = reverse(summ)
print("Сумма наоборот:", reverse_summ)
