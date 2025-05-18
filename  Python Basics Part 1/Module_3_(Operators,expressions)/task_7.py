number = int(input("Введите пожалуйста четырехзначное число:"))
first_class = number//1000
second_class = number//100 - first_class * 10
third_class = number//10 - second_class * 10 - first_class * 100
fourth_class = number//1 - third_class * 10 - second_class *100 - first_class *1000
print("Первый разряд:", first_class, "\nВторой разряд:", second_class, "\nТретий разряд:", third_class, "\nЧетвертый разряд:", fourth_class)