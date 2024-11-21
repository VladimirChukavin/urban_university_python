# Дополнительное практическое задание по модулю
import math


class Figure:
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта геометрической фигуры
    """
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = list(sides)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        is_positive_int = all([isinstance(x, int) for x in new_sides]) and all([x > 0 for x in new_sides])
        return is_positive_int and len(new_sides) == self.sides_count

    def check_sides(self, *new_sides):
        if not self.__is_valid_sides(new_sides):
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта круга
    """
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.check_sides(*sides)
        self.__sides = self.get_sides()
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius * self.__radius


class Triangle(Figure):
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта треугольника
    """
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.check_sides(*sides)
        self.__sides = self.get_sides()

    def get_square(self):
        half_perimeter = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        square_triangle = math.sqrt(
            half_perimeter * (half_perimeter - self.__sides[0]) * (half_perimeter - self.__sides[1]) * (
                    half_perimeter - self.__sides[2]))
        return round(square_triangle, 2)


class Cube(Figure):
    """
    Класс, содержащий необходимые атрибуты и методы для создания объекта куба
    """
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_cube_sides(sides)
        self.__sides = self.get_sides()

    def set_cube_sides(self, sides):
        if len(sides) == 1:
            cube_sides = [sides[0] for _ in range(self.sides_count)]
            self.check_sides(*cube_sides)
        else:
            self.check_sides(*sides)

    def get_volume(self):
        return int(math.pow(self.__sides[0], 3))


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
