class Road:

    def __init__(self, _length, _width, mass, h):
        self._length = _length
        self._width = _width
        self.mass = mass
        self.h = h
        print(_length * _width * mass * h / 1000,'тонн')

mass_road = Road(20, 5000, 25, 5)
mass_road_2 = Road(50, 5500, 23, 10)

