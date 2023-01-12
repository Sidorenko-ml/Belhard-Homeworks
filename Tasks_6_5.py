# Сериальзовать объект при помощи библиотеки pydantic
from pydantic import BaseModel, ValidationError


data = {
'age': 45,
'name': 'Peter',
'children': [
    {   'age': 3,
        'name': 'Alice'}
],
'married': True,
'city': None}


class Children(BaseModel):
    age : int
    name : str


class Base(BaseModel):
    age : int
    name : str
    children : list[Children]
    married : bool
    city : None


try:
    rez = Base.parse_obj(data)
except ValidationError as e:
    print('Exception', e.json())

print(rez)