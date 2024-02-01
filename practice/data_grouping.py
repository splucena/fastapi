from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel


# tuple
# list
# dict

CreateNamedTuple = namedtuple(
    "CreateNamedTuple", "name, country, area, description, aka"
)
namedtuple_thing = CreateNamedTuple(
    "yeti", "CN", "Himalaya", "Hirsute Himalayan", "Snowman"
)
print("Name is", namedtuple_thing[0])
# Name is yeti
print("Name is", namedtuple_thing.name)


# Standard class
class CreatureClass:
    def __init__(self, name: str, country: str, area: str, description: str, aka: str):
        self.name = name
        self.country = country
        self.area = area
        self.description = description
        self.aka = aka


class_thing = CreatureClass("yeti", "CN", "Himalaya", "Hirsute Himalayan", "Snowman")
print("Name is", class_thing.name)
# Name is yeti


@dataclass
class CreatureDataClass:
    name: str
    country: str
    area: str
    description: str
    aka: str


dataclass_thing = CreatureDataClass(
    "yeti", "CN", "Himalaya", "Hirsute Himalayan", "Snowman"
)
print("Name is", dataclass_thing.name)
# Name is yeti


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


thing = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsuite Himalayan",
    aka="Snowman",
)
print("Name is", thing.name)


creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsuite Himalayan",
        aka="Snowman",
    ),
    Creature(
        name="yeti2",
        country="CN",
        area="Himalayas",
        description="Hirsuite Himalayan",
        aka="Snowman",
    ),
]

def get_creatures() -> list[Creature]:
    return creatures

print("Creatures", creatures)
