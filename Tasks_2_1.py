class InconsistentDataError(Exception):
    pass


try:
    katets_a = []
    katets_b = []
    while True:
        katets_a.append(int(input("Введите значения для катета а - ")))
        katets_b.append(int(input("Введите значения для катета b - ")))
except:
    if len(katets_a) != len(katets_b):
            raise InconsistentDataError
    gip = [(((a**2)+ (b**2))**0.5) for a,b in zip(katets_a,katets_b)]
    s = [((a*b)/2) for a,b in zip(katets_a,katets_b)]
    for a, b, item, items in zip(katets_a, katets_b, gip, s):
        print(f'Треугольник с катетами {a} и {b} имеет площадь {items} и гипотенузу {item}')


