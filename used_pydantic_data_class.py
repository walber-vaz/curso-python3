from pydantic import StrictInt, StrictStr
from pydantic.dataclasses import dataclass


@dataclass
class Person:
    name: StrictStr
    age: StrictInt


user = Person(name='John Doe', age=20)
print(user)
