import math

class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides, filled = False):
        self.filled = filled
        self.__color = __color
        if len(__sides) == self.sides_count:
            self.__sides = list(__sides)
        else:
            self.__sides = [1] * self.sides_count
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if r in range(255) and g in range(255) and b in range(255):
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *args):
        valid = True
        for i in args:
            if not isinstance(i, int) or i < 0:
                valid = False
        if len(args) != self.sides_count:
            valid = False
        return valid
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, *__sides, filled = False):
        super().__init__(__color, *__sides, filled = False)
        self.__radius = __sides[0] / math.pi
    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        p = self.__len__() / 2
        return (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *__sides, filled = False):
        super().__init__(__color, *__sides, filled = False)
        self.__sides = list(__sides) * 12
    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())