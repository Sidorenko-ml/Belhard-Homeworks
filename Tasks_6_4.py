import yaml


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }}


data1 = yaml.dump(data) # Сериализуем в строку

with open('Tasks_6_4.yaml', "w") as f:
    data_1 = yaml.dump(data, f)


with open('Tasks_6_4.yaml', "r") as f2:
    des = yaml.load(f2, Loader=yaml.FullLoader) # Десериализация из файла

data2 = yaml.load(data1,Loader=yaml.FullLoader) # Десериализуем из строки

print(des)


