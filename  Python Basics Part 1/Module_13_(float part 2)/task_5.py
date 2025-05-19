amplitude = float(input('Введите начальную амплитуду: '))
amplitude_stop = float(input('Введите амплитуду остановки: '))


def amp(amplitude, amplitude_stop):
    stop = 1
    stopping = 0
    damping = 8.4 / 100
    while stop > amplitude_stop:
        stop *= 1 - damping
        stopping += 1
    print('Маятник считается остановившимся через', stopping, 'колебаний')


amp(amplitude, amplitude_stop)