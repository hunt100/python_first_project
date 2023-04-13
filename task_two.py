# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)

class MetaSingleton(type):

    _Worker = None

    def __call__(cls, *args, **kwargs):
        if cls._Worker is None:
            cls._Worker = super().__call__()
            return cls._Worker
        else:
            return cls._Worker


class Road(metaclass=MetaSingleton):

    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length


road_1 = Road()
road_2 = Road()
print(road_1 is road_2)
