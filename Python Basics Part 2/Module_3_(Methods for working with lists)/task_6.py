#Задание 6. Уникальное объединение списков
#Контекст
#Вы работаете в команде разработки программного обеспечения для компании, которая занимается обработкой и анализом данных. Ваша команда получает данные из различных источников, вам нужно объединить их в один отсортированный список для дальнейшей обработки. Однако источники данных возвращают отсортированные списки с возможными дубликатами, и ваша задача — создать программу, которая объединит эти списки в один отсортированный список без дубликатов.

#Задача
#Напишите программу, которая объединяет два отсортированных списка целых чисел в один отсортированный список без дубликатов.

#Пример:
#list1 = [1, 3, 5, 7, 9]
#list2 = [2, 4, 5, 6, 8, 10]
#merged = merge_sorted_lists(list1, list2)
#print(merged)
#Вывод в консоли:
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or list2[j] != merged[-1]:
                merged.append(list2[j])
            j += 1
        else:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        if not merged or list1[i] != merged[-1]:
            merged.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged or list2[j] != merged[-1]:
            merged.append(list2[j])
        j += 1

    return merged


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)