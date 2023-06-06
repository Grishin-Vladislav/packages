from application.stuff.parser import RandomHuman


class Employee:
    def __init__(self):
        for key, value in RandomHuman().data.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)