# Написать декоратор inspect, который при вызове функции печатает входные
# параметры и возвращаемое значение, обернуть в него функцию concat


def inspect(func):
    def wrapped(*args,**kwargs):
        print(f""" 
        Args: {args}\n
        Kwargs: {kwargs}\n 
        """)
        return func(*args,**kwargs)    
    return wrapped


@inspect
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