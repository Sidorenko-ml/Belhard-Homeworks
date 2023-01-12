from collections import Counter


persons = [{"name" : "Anna", 
            "age" : "25", 
            "gender" : "female"},

            {"name" : "Aleksandr", 
            "age" : "29", 
            "gender" : "male"},

            {"name" : "Marina", 
            "age" : "34", 
            "gender" : "female"},

            {"name" : "Ilya", 
            "age" : "17", 
            "gender" : "male" },

            {"name" : "Aleksandr", 
            "age" : "59", 
            "gender" : "male"},

            {"name" : "Fedor", 
            "age" : "50", 
            "gender" : "male"},

            {"name" : "Viktoriya", 
            "age" : "24", 
            "gender" : "female"}]
NumbofPeople = len(persons)
print("Количество всех людей: ", NumbofPeople)
Women = []
Men = []
for item in persons[0:7]:
    if item["gender"] == "female":
        Women.append("female")
    else:
        Men.append("male")
print("Количество женщин - ", len(Women))
print("Количество мужчин - ", len(Men))
Sovershennoletniye = []
for item in persons[0:7]:
    if item["age"] > "18":
        Sovershennoletniye.append("1")
print("Количество совершеннолетних персон - ", len(Sovershennoletniye))
Names = []
for item in persons:
    Names.append(item["name"])
print(Names)
Vosrast = []
for item in persons:
    Vosrast.append(item["age"])
    Vosrast.sort()
print(Vosrast)
counter = Counter(Names)
print(counter.most_common(1))
for item in persons:
    if (item["age"] > "35") and (item['name'][0] == 'F'):
        print(f"Имя человека, чей возраст больше 35 лет и имя начинается на F - {item['name']}")