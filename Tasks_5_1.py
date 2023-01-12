# Написать CLI (Command line interface) приложение (argparse либо click), которая умеет:
# Считать кол-во дней до нового года (при помощи параметра --hours, так же часов)

import click
import datetime
from loguru import logger
import enum
import random

logger.add("logs.log", format="{time} {level} {message}", level="DEBUG")


@click.command()
@click.argument('newyear')
@click.option('--hours', "-h", is_flag = True, help="Show us number of days and hours to New Year")
def get_number_of_days(newyear, hours):
    """ This function show us number of days to New Year """
    if newyear != "newyear":
        logger.debug("Exception in CLI, incorrect command")
        raise Exception('Incorrect command')
    elif hours:
        newyear = datetime.datetime(2022,12,31,23,59,59)
        today = datetime.datetime.now()
        numbers = newyear - today
        return print(f'Колмчество дней до Нового Года - {numbers.days} days,{(numbers.seconds//3600)} hour')  
    else:
        newyear = datetime.date(2023,12,31)
        today = datetime.date.today()
        numbers = newyear - today
        return print(f'Количество дней до Нового Года - {numbers.days}')


if __name__ == "__main__":
    get_number_of_days()