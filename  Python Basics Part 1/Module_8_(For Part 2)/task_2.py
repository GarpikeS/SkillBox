#«МирПрогБанк» наконец-то разделил законопослушных граждан и должников и поместил их в разные базы. Но банк не торопится сильно давить на неплательщиков. Операторам банка дали задание позвонить каждому пятому должнику из списка (нумерация начинается с нуля) и уточнить, какую сумму каждый из них задолжал банку.

#Напишите программу, которая получает данные о количестве должников, а затем спрашивает у каждого пятого (начиная с нуля) его долг. В конце выводится общая сумма долгов.
duters = int(input("Введите колличество должников:"))
check = 0
summ = 0
for check in range(0,duters,5):
    duty = int(input("Введите размер вашего долга:"))
    summ = summ + duty
print("Общая сумма долга:",summ)