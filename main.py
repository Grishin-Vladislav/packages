from application.salary import calculate_salary
from application.db.people import get_people

if __name__ == '__main__':
    print('entry point: __main__')
    calculate_salary()
    print('Active workers:')
    get_people(4)
