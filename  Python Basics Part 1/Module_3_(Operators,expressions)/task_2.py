#Запросить у пользователя четыре числа.
#Отдельно сложить два первых и два вторых.
#Разделить первую сумму на вторую.
#Вывести результат на экран.
first_number = int(input("Введите пожалуйста сумму дохода первого квартала:"))
second_number = int(input("Введите пожалуйста сумму дохода второго квартала:"))
third_number = int(input("Введите пожалуйста сумму дохода предпоследнего квартала:"))
fourth_number = int(input("Введите пожалуйста сумму дохода последнего квартала:"))
summ_first = first_number + second_number
summ_last = third_number + fourth_number
result = summ_first/summ_last
print(result)