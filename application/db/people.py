from application.stuff.staff import Employee
from time import sleep
from tqdm import tqdm
from tabulate import tabulate


def get_people(amount=1):
    headers = (
        'name', 'surname', 'gender', 'age', 'birth date',
        'height', 'weight', 'blood type'
    )
    employees = []
    for _ in tqdm(range(amount), colour='green',
                  desc='Getting workers from database...'):
        employees.append(field for field in Employee().__dict__.values())
        sleep(1)
    print(tabulate(employees, headers, 'presto'))
