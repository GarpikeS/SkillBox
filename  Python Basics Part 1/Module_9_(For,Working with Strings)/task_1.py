#Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».
check = 0
first_check = "Карамба"
second_check = "карамба"
for score in range(10):
  text = input("Введите пожалуйста 10 слов:")
  for word in text:
    if text == first_check or text == second_check:
      check += 1
print("Со словом карамба совпадает:", check/7)
