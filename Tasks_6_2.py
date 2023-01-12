# Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle-

import pickle


class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_values(self):
        print(f"{self.name=}")
        print(f"{self.age=}")

# with open('data.pickle', 'wb') as f: #Выгружаем в файл
#     pickle.dump(User, f)

with open('data.pickle', 'rb') as f:
    user = pickle.load(f)   # Доступ к объекту класса через файл

first_user = user('Alex', 10)
first_user.get_values()


# pickle.dump() - позволяет записывать внутрь файла
# pickle.dumps() - позволяет записывать внутрь переменной
# a = {'first': 'a', 'second' : 2, 'third' : [1,2,3]}
# b = pickle.dumps(a)
# print(b)
# pickle.load() выгружает из файла
# pickle.loads() выгружает из переменной