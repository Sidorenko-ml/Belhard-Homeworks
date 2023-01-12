# Создать функцию concat, которая принимает неограниченное кол-во
# параметров-строк, скливает их и возвращает. Опционально может принимать
# именнованный параметр reversed: bool и при reversed=True склеивание
# начинает с конца списка параметров.


def concat(*args, reversed = False):
    sp = []
    for i in args:
        sp.append(i)
    sp_str = ' '.join(sp)
    if reversed == False:
        print(sp_str)
    else:
        sp.reverse()
        sp_str = ' '.join(sp)
        print(sp_str)

concat('Hi','','world', reversed=True)