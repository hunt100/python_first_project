# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, mass_per_single_part, thickness):
        try:
            return self._length * self._width * mass_per_single_part * thickness
        except TypeError:
            return None


road_length = float(input("Input road length: "))
road_width = float(input("Input road width: "))
mass_per_one_road_part = float(input("Input mass of road for singular part: "))
road_thickness = float(input("Input road thickness"))

road = Road(road_length, road_width)
print(f"{road_length}m * {road_width}m * {mass_per_one_road_part}kg * {road_thickness}m ="
      f" {road.calculate_mass(mass_per_one_road_part, road_thickness)}kg ="
      f" {road.calculate_mass(mass_per_one_road_part, road_thickness) / 1000}t")
