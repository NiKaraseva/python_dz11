class Archiv:
    """Создаём класс Archiv, который хранит пару свойств: число и строку.
    При создании нового экземпляра класса старые данные из ранее созданных
    экземпляров сохраняются в пару списков-архивов.
    list-архивы также являются свойствами экземпляра"""

    instance = None

    def __init__(self, num: int, string: str):
        """Инициализируем первоначальные данные: число и строку."""
        self.num = num
        self.string = string

    def __new__(cls, *args, **kwargs):
        """При добавлении новых параметров сперва проверяем, существуюли ли списки.
        Если нет – создаём их, если да – добавляем данные в списки.
        Число в список cls.instance.old_num, строку – в список cls.instance.old_string"""

        if cls.instance:
            cls.instance.old_num.append(cls.instance.num)
            cls.instance.old_string.append(cls.instance.string)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_num = []
            cls.instance.old_string = []
        return cls.instance

    def __repr__(cls):
        """Технический вывод результата для программиста"""

        return f'Archiv({cls.instance.old_num = }, {cls.instance.old_string = })'

    def __str__(cls):
        """Удобный вывод результата для пользователя"""

        return f'Список номеров: {cls.instance.old_num}, список строк: {cls.instance.old_string}'


if __name__ == '__main__':
    a1 = Archiv(22, 'Ёу')
    a2 = Archiv(11, 'Ёуёу')
    a3 = Archiv(10, 'Ку')

    print(repr(a3))
    print(a3)