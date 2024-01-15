# task 1
class Soda:

    def __init__(self, taste,):
        self.taste = taste

    def my_drink(self, my_drink):
        self.my_drink = my_drink


my_drink = Soda(taste='Straberry')
print(my_drink.taste)
my_drink = Soda(taste='No taste')
print(my_drink.taste)

# task 2


class Math:
    def __init__(self, a, b, example):
        self.a = a
        self.b = b
        self.example = example

    def __add__(self):
        print(self.a + self.b)

    def __mul__(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)
# task 3


class Car:

    car_count = 0

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        Car.car_count += 1

    def start(self):
        print('The car is started')

    def stop(self):
        print('The car is turned off')

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year


car_a = Car(color='blue', type='sportcar', year=2005)
car_a.start()
print(car_a.car_count)
car_a.stop()

car_b = Car(color='yellow', type='liftback', year=2017)
car_b.start()
print(car_b.car_count)

car_c = Car(color='red', type='family', year=2000)
car_c.start()
print(car_c.car_count)
car_c.stop()

# task 4
from math import pi


class Sphere:
    def __int__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            raise TypeError
        self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4/3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2


some = Sphere()
print(some.get_volume)
print(some.get_radius)
print(some.get_center)
print(some.set_center)

# task 5


class SuperStr:
    def is_repeatance(self, s):
        if not isinstance(s, str):
            return False
        n = len(self) % (len(s) or 1)
        return self == n * s
    def is_palindroma(self):
        s = self.lower()
        return s == s[::-1]