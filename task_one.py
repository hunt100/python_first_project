# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
#
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
#
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
#
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep


class TrafficLight:

    __color = ""

    def running(self, g_time):
        states = {"red": 7, "yellow": 2, "green": g_time}
        while True:
            for color, time in states.items():
                self.__color = color
                print(f"Current color: {self.__color}")
                sleep(time)


my_traffic_light = TrafficLight()
my_traffic_light.running(int(input("Input green light time: ")))
