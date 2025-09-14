#Задание 9. Ролики
#Что нужно сделать
#Частная контора даёт в прокат ролики самых разных размеров. Человек может надеть ролики только своего размера.

#Пользователь вводит два списка размеров: N размеров роликов и K размеров ног людей. Реализуйте код, который определяет, какое наибольшее число человек может одновременно взять ролики и пойти кататься.

#Пример:

#Количество роликов: 4
#Размер пары 1: 41
#Размер пары 2: 40
#Размер пары 3: 39
#Размер пары 4: 42

#Количество людей: 3
#Размер ноги человека 1: 42
#Размер ноги человека 2: 41
#Размер ноги человека 3: 42
#Наибольшее количество людей, которые могут взять ролики: 2

def max_people_with_skates(skates_sizes, people_sizes):
    skates_sizes.sort()
    people_sizes.sort()
    count = 0
    i = j = 0
    while i < len(skates_sizes) and j < len(people_sizes):
        if skates_sizes[i] == people_sizes[j]:
            count += 1
            i += 1
            j += 1
        elif skates_sizes[i] < people_sizes[j]:
            i += 1
        else:
            j += 1
    return count

rollers = int(input("Количество роликов: "))
skates = []
for i in range(rollers):
    size = int(input(f"Размер пары {i + 1}: "))
    skates.append(size)

number_people = int(input("Количество людей: "))
people = []
for i in range(number_people):
    size = int(input(f"Размер ноги человека {i + 1}: "))
    people.append(size)

result = max_people_with_skates(skates, people)
print("Наибольшее количество людей, которые могут взять ролики:", result)

