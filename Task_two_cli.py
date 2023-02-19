"""
The task 2 goes like following:
Pull data for the first movie in star wars
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

import argparse


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(FIRST_FILM_URL)

    result_ = response.json()

    write_data_into_file(result_)
    return result_


def second_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""
    names = []
    characters = data_.get("{}".format(object1.people))  # returns None by default

    for character in characters:
        character_data = hit_url(character)
        character_data = character_data.json()
        names.append(character_data.get("name"))

    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     names.append(character.get("name"))

    return names


def third_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""

    planets = data_.get("{}".format(object1.planet))  # returns None by default

    planets_names = []
    for planet in planets:
        planets_data = hit_url(planet)
        planets_data = planets_data.json()
        planets_names.append(planets_data.get("name"))

    return planets_names


def fourth_task(data_: Dict) -> List:
    """pull data from swapi characters sequentially"""

    vehicles = data_.get("{}".format(object1.vehicle))  # returns None by default

    vehicles_names = []
    for vehicle in vehicles:
        vehicles_data = hit_url(vehicle)

        vehicles_data = vehicles_data.json()
        vehicles_names.append(vehicles_data.get("name"))

    return vehicles_names


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--films", "--FILMS")
    parser.add_argument("--people", "--PEOPLE")
    parser.add_argument("--planet", "--PLANET")
    parser.add_argument("--vehicle", "--VEHICLE")

    object1 = parser.parse_args()

    FIRST_FILM_URL = "https://swapi.dev/api/films/{}/".format(object1.films)

    # first task
    first_result = first_task()
    pprint(first_result)

    # second task
    second_result = second_task(first_result)
    pprint(second_result)

    # third result
    third_result = third_task(first_result)
    pprint(third_result)

    # fourth result
    fourth_result = fourth_task(first_result)
    pprint(fourth_result)