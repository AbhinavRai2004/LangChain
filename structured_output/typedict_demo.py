from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

newp: Person = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com'
    }

print(newp)