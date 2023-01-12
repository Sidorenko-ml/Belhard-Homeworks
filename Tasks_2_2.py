class InconsistentDataError(Exception):
    pass


sp = []
while 1==1:
    a = input("Введите поочередно значения для катетов a и b - ")
    print("Чтобы закончить ввод нажмите 'q'")
    if a == 'q':
        break
    else:
        sp.append(a)
if (len(sp) % 2 != 0):
        raise InconsistentDataError('Некорректно введены данные катетов треугольников')
else:
    
    chet = sp[1::2]
    nechet = sp[0::2]
    gip = [(((int(a)**2) + (int(b)**2))**0.5) for a,b in zip(nechet,chet)]
    s = [((int(a)*int(b)/2)) for a,b in zip(nechet,chet)]
    for a, b, item, items in zip(nechet, chet, gip, s):
        print(f'Треугольник с катетами {a} и {b} имеет площадь {items} и гипотенузу {item}')
