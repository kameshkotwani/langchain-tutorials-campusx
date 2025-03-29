from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person :Person = {'age': 30, 'name': 35}
print(new_person)