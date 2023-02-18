"""
The task 2 goes like following:
Pull data for the  first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data


FIRST_FILM_URL = "https://swapi.dev/api/films/1/"    # for getting first movie


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))     # converts data into json string


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()  # data from link gets extracted here in the form of json string
    write_data_into_file(result_)  # this refers to above function, and puts extracted data in 'data'
    return result_


def second_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""

    characters = data_.get("characters")  # returns None by default

    names = []
    for character in characters:
        character_data = hit_url(character)
        character_data = character_data.json()
        names.append(character_data.get("name"))

    # names = []
    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     names.append(character.get("name"))

    return names


def third_task(data_: Dict) -> List:
    """pull data from swapi planets sequentially"""

    planets = data_.get("planets")  # returns None by default

    names = []
    for planet in planets:
        planet_data = hit_url(planet)
        planet_data = planet_data.json()
        names.append(planet_data.get("name"))

    return names


def fourth_task(data_: Dict) -> List:
    """pull data from swapi vehicles sequentially"""

    vehicles = data_.get("vehicles")  # returns None by default

    names = []
    for vehicle in vehicles:
        vehicle_data = hit_url(vehicle)
        vehicle_data = vehicle_data.json()
        names.append(vehicle_data.get("name"))

    return names


if __name__ == "__main__":

    # first task
    first_result = first_task()  # object creation of first_task()
    pprint(first_result)

    # second task : capture characters
    second_result = second_task(first_result)
    pprint(second_result)

    # third task : capture planets
    third_result = third_task(first_result)
    pprint(third_result)

    # Fourth task : capture vehicles
    fourth_result = fourth_task(first_result)
    pprint(fourth_result)             #pprint for printing properly