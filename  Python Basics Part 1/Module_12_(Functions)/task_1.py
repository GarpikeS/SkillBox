N = int(input('Введите число N:'))
def summa_n(N):
    if N==0:
        return N
    else:
        return(N+summa_n(N-1))
print("Сумма чисел от 1 до",N," = ",summa_n(N))