import math

class Rectangle:
    """Создали класс Rectangle, который создаёт экземпляр прямоугольника
     с длиной length и шириной width (если length = width – у нас куб) .
     Внутри класса есть функции:
     – по расчёту периметра прямоугольника,
     – по расчёту площади прямоугольника,
     – переинициализирована функция сложения,
     – переинициализирована функция вычитания,
     – добавлены функции сравнения прямоуголников.
     """

    _pi = math.pi


    def __init__(self, length, width=None) -> None:
        """Инициализировали стороны прямоуголника: length и width"""

        self.length = length
        if width:
            self.width = width
        else:
            self.width = length


    def calc_perimeter(self):
        """Функция по расчёту периметра прямоугольника"""

        return (self.length + self.width) * 2

    def calc_area(self):
        """Функция по расчёту площади прямоугольника"""

        return self.length * self.width


    def __add__(self, other):
        """Переинициализирована функция сложения двух прямоуголников"""

        return Rectangle(length=
                         (self.length + other.length),
                         width=self.width)

    def __sub__(self, other):
        """Переинициализирована функция вычитания двух прямоуголников"""

        return Rectangle(length=
                         abs(self.length - other.length),
                         width=self.width)


    def __eq__(self, other: "Rectangle"):
        """Проверяет на равенство прямоугольников"""

        return self.calc_area() == other.calc_area()

    def __lt__(self, other: "Rectangle"):
        """Проверяет, меньше ли первый прямоуголник второго"""

        return self.calc_area() < other.calc_area()

    def __le__(self, other: "Rectangle"):
        """Проверяет, меньше или равен первый прямоуголник второго"""

        return self.calc_area() <= other.calc_area()

    def __gt__(self, other: "Rectangle"):
        """Проверяет, больше ли первый прямоуголник второго"""

        return self.calc_area() > other.calc_area()

    def __ge__(self, other: "Rectangle"):
        """Проверяет, больше или равен первый прямоуголник второго"""

        return self.calc_area() >= other.calc_area()


    def __repr__(self):
        """Технический вывод результата для программиста"""

        return f'Rectangle({self.length = }, ' \
               f'{self.width = }, ' \
               f'{self.calc_perimeter() = } ' \
               f'{self.calc_area()})'

    def __str__(self):
        """Удобный вывод результата для пользователя"""

        return f'Длина прямоугольника = {self.length}, ' \
               f'ширина прямоугольника = {self.width}, ' \
               f'периметр = {self.calc_perimeter()}, ' \
               f'площадь = {self.calc_area()}'



if __name__ == '__main__':
    r1 = Rectangle(2, 1)
    print(repr(r1))
    print(r1)

    r2 = Rectangle(3)
    print(repr(r2))
    print(r2)

    r3 = r2 + r1

    print('---')
    print(repr(r3))
    print(r3)

    print(r3 > r1)
    print(r2 == r1)
    print(r3 >= r1)