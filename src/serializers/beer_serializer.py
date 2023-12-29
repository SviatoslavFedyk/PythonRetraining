import json
from src.models.beer_model import Beer, BeerTuple

def serialize_beer_class(beers):
    list_beers = []
    for beer in beers:
        valid_keys = ['id', 'name', 'description', 'abv']
        filtered_data = {key: beer[key] for key in valid_keys}
        list_beers.append(Beer(**filtered_data))
    return list_beers

def serialize_beer_namedtuple(beers):
    list_beers = []
    for beer in beers:
        valid_keys = ['id', 'name', 'description', 'abv']
        filtered_data = {key: beer[key] for key in valid_keys}
        list_beers.append(BeerTuple(**filtered_data))
    return list_beers

def serialize_beer_dynamic_class(beers):
    list_beers = []
    for beer in beers:
        Beer = type(beer['name'], (object,), beer)
        list_beers.append(Beer)
    return list_beers