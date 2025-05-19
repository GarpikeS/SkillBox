import random


def rock_paper_scissors():
    comp = random.SystemRandom().choice(['камень', 'ножницы', 'бумага'])
    user = input("Введите камень, ножницы или бумага: ")
    if user == "камень" and comp == "ножницы":
        print("Компютер выбрал:", comp)
        print("Вы победили")
    elif user == "камень" and comp == "бумага":
        print("Компютер выбрал:", comp)
        print("Вы проиграли")
    elif user == "ножницы" and comp == "камень":
        print("Компютер выбрал:", comp)
        print("Вы проиграли")
    elif user == "ножницы" and comp == "бумага":
        print("Компютер выбрал:", comp)
        print("Вы выйграли")
    elif user == "бумага" and comp == "ножницы":
        print("Компютер выбрал:", comp)
        print("Вы проиграли")
    elif user == "бумага" and comp == "камень":
        print("Компютер выбрал:", comp)
        print("Вы выйрали")
    else:
        print("Компютер выбрал:", comp)
        print("Ничья")


def guess_the_number():
    while True:
        comp = random.randint(1, 10)
        user = int(input("Введите число от 1 до 10:  "))
        if comp != user:
            print("Компютер загадал число:", comp)
            print("Вы не отгадали, попробуйте еще раз:")
            print()
        else:
            print("Компютер загадал число:", comp)
            print("Вы отгадали. Молодец.")
            print("Игра завершена.")
            break


def mainMenu():
    give = int(input("Выберите игру:\n 1) Камень.Ножницы.Бумага.\n 2) Угадай число.\n Ваш выбор:"))
    if give == 1:
        print()
        rock_paper_scissors()
    elif give == 2:
        print()
        guess_the_number()
    else:
        print('Неправильный выбор. Выберите игру.')
        mainMenu()


mainMenu()