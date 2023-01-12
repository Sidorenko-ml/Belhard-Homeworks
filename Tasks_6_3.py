# Сериализовать объект при помощи json и yaml и десериализовать в/из строки и файла
import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f) #Запись данных в файл

new_object = json.dumps(data) # Преобразуется в строку


with open('data.json', 'r') as f2:  # Выгружаем данные из файла
    read_file = json.load(f2)

print(read_file)

data2 = json.loads(new_object) # Читаем из строки
print(data2)