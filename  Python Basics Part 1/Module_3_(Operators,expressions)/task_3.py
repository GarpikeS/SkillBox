#Напишите программу, которая получает от пользователя число и выводит на экран два ответа — следующее и предыдущее числа.
number = int(input("Введите пожалуйста число:"))
before_number = number - 1
after_number = number + 1
print("После числа", number, "идет число", after_number, "\nДо числа", number, "идет число", before_number)
