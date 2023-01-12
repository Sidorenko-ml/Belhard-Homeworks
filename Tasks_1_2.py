a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

first = ((a**2) + (b**2)) / ((3*b) -4)
second = (4*(c**5))/6
rez1 = print(f'Целая часть - {first // second}')
rez2 = print(f'Остаток от деления - {first % second}')