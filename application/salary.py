from datetime import datetime as d
from datetime import timedelta
from time import sleep

var = d.now
date_template = '%d-%m-%y %H:%M:%S'


def calculate_salary():
    start_date = d.now()

    print(f'{start_date.strftime(date_template)} | doing calculations...')

    sleep(1)
    delta = timedelta(seconds=1)
    upd_date = start_date + delta

    print(
        f'{upd_date.strftime(date_template)}'
        f' | result: {999999 - int(var().microsecond)}'
    )
