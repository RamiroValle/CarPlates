#!/usr/bin/env python
import sys
import random
import json
from os.path import exists
from string import ascii_uppercase, digits

cars: list = [
    "Ford", "Peugeot", "Chevrolet", "BMW", "Alfa Romeo", "Cadillac", "Citroën", "Hyundai", "Ferrari", "Renault"
]

models: list = [
    "A3", "A4", "Civic", "Challenger", "Crosstrek", "Encore", "Explorer", "Fit", "Golf", "Insight", "Maxima", "Niro"
]


def main(name: str = "example.json", entries: int = 10000):
    def make_model() -> str:
        """Generates a random car name/model from a random car and a random model"""
        return f"{random.choice(cars)} {random.choice(models)}"

    def make_plate() -> str:
        """Generates a random plate with the format 'XXX yyy' where x is a random A-Z letter and y is
            a random number between 0-9"""
        return f"{random.choice(ascii_uppercase)}{random.choice(ascii_uppercase)}{random.choice(ascii_uppercase)} " \
               f"{random.choice(digits)}{random.choice(digits)}{random.choice(digits)}"

    if not exists(name):
        car_entries = dict({(make_plate(), make_model()) for n in range(entries)})
        with open(name, "w") as f:
            json.dump(car_entries, f)


if __name__ == '__main__':
    try:
        main(name=sys.argv[1], entries=int(sys.argv[2]))
    except IndexError:
        try:
            main(name=sys.argv[1])
        except IndexError:
            main()
