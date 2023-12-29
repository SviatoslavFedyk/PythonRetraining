from collections import namedtuple
class Beer:
    def __init__(self, id, name, description, abv):
        self.id = id
        self.name = name
        self.description = description
        self.abv = abv

BeerTuple = namedtuple("BeerTuple", ["id", "name", "description", "abv"])