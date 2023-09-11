import time


class MyStr(str):
    """Создаём класс MyStr, которому доступны все возможности родительского класса str
    с дополнительным хранением имени автора строки и времени создания (через time.time)."""

    def __new__(cls, value: str, name: str):
        """Инициализировали класс str и добавили внутри 2 новых параметра:
        name (имя автора) и time_creating (время создания)"""

        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time_creating = time.time()
        return instance

    def __repr__(self):
        """Технический вывод результата для программиста"""

        return f'MyStr({self.value = }, {self.name = }, {self.time_creating = })'

    def __str__(self):
        """Удобный вывод результата для пользователя"""

        return f'Строка: {self.value}, имя автора: {self.name}, время создания: {self.time_creating}'


if __name__ == '__main__':
    str1 = MyStr('Моя строка', name='Ника')
    print(repr(str1))
    print(str1)





