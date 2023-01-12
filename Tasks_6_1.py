# Записать в файл строку, потом её считатm

with open('Tasks_6_1.txt', 'w') as f:
    f.writelines('Записываю строку для дальнейшего считывания')

with open('Tasks_6_1.txt', 'r') as f2:
    print(f2.readline())