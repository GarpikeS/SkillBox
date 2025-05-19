def reverse():
    first_number = int(input("Введите целое число: "))
    reverse_number = 0
    while first_number > 0:
        digit = first_number % 10
        first_number = first_number // 10
        reverse_number = reverse_number * 10
        reverse_number = reverse_number + digit

    print('"Обратное" ему число:', reverse_number)


reverse()