check = 0
total = 0
for check in range(12):
 money = int(input("Введите запрплату за месяц"))
 total = total + money
average = total/12
print("Средняя зарплата сотрудника за год:",average)