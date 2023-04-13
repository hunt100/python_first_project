#1) реализовать дескрипторы для любых двух классов

class ReadOnlyAttribute:

    def __set__(self, instance, value):
        msg = 'You cannot change [{}]. It is read only attribute. Try to change to value {}'.format(self.name, value)
        raise AttributeError(msg)

    def __set_name__(self, owner, name):
        self.name = name

class TrafficLight:

    _color = ''
    g_time = ReadOnlyAttribute()

    def running(self, g_time):
        states = {"red": 7, "yellow": 2, "green": g_time}
        for i in range(g_time):
            for color, time in states.items():
                self._color = color
                print(f"Current color: {self._color}")


my_traffic_light = TrafficLight()
my_traffic_light.running(int(input("Input green light time: ")))

# Exception will be raised
# my_traffic_light.g_time = 12


class NonNull:

    def __set__(self, instance, value):
        if value == '':
            raise ValueError(f"Value for field [{self.name}] is missing")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Worker:

    name = NonNull()
    surname = NonNull()
    position = NonNull()
    _income = None

    def __init__(self, name, surname, position, wage=0.0, bonus=0.0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

    def get_full_name(self):
        return self.surname + self.name

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f"{self.surname} {self.name} - {self.position} [{self.get_total_income()}]"


worker = Worker("Name", "Surname", "Position", 10.0, 2.0)
# Exception will be raised
# another_worker = Worker("", "Surname", "Position", 10.0, 2.0)
