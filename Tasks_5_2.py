# Написать CLI (Command line interface) приложение (argparse либо click), которая умеет:
# Случайно выбирает какую вам купить игрушку для ёлки (enum + random) с двумя параметрами

import click
import datetime
from loguru import logger
import enum
import random


logger.add("logs.log", format="{time} {level} {message}", level="DEBUG")


class Colors(enum.Enum):
    Red = 7
    Blue = 6
    Green = 5
    Yellow = 4
    Purple = 3
    Orange = 2
    Violet = 1

class Toys(enum.Enum):
    Ball = 7
    Angel = 6
    Rabbit = 5
    Gingerbread = 4
    Star = 3
    Stocking = 2
    Lights = 1


@click.command()
@click.argument('toy')
def get_item(toy):
    """This function shows us which toy to buy"""
    one = random.randrange(1, 7)
    two = random.randrange(1, 7)
    return print(f"{Colors(one).name} {Toys(two).name}")


if __name__ == "__main__":
    get_item()