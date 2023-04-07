# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
#
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

class Worker:

    name = ""
    surname = ""
    position = ""
    _income = None

    def __init__(self, name, surname, position, wage=0.0, bonus=0.0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.surname + self.name

    def get_total_income(self):
        return sum(self._income.values())

    def __str__(self):
        return f"{self.surname} {self.name} - {self.position} [{self.get_total_income()}]"


name = input("Input name: ")
surname = input("Input surname: ")
position = input("Input position: ")
wage = float(input("Input wage: "))
bonus = float(input("Input bonus: "))

position = Position(name, surname, position, wage, bonus)
print(position.name)
print(position.surname)
print(position.position)
print(position.get_full_name())
print(position.get_total_income())
print(position)
