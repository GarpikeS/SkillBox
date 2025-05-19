word = input('Введите зашифрованое слово: ')
sum1 = ' '
sum2 = ' '
check = 0
for text in word:
    check += 1
    if (check % 2 == 1):
        sum1 += text
    else:
        sum2 = text + sum2
print('Расшифрованое слово', sum1 + sum2)