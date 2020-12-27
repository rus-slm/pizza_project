import random


class MainPizza:

    def __init__(self, size='L'):
        """Определяем возможные ингредиенты пиццы и размер"""
        self.tomato_sause = True
        self.mozzarella = True
        self.tomatoes = False
        self.pepperoni = False
        self.chiken = False
        self.pineapples = False
        self.spinach = False
        if size == 'XL':
            self.size = 'XL'
        else:
            self.size = 'L'

    def dict(self):
        """Возвращаем список ингредиентов"""
        return ', '.join(list({key: value for key, value in self.__dict__.items()
                               if value and key is not 'size'}.keys()))


class Margherita(MainPizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.tomatoes = True


class Pepperoni(MainPizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.pepperoni = True


class Hawaiian(MainPizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.chiken = True
        self.pineapples = True


class Spinach(MainPizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.spinach = True


def log(function):
    def func():
        return f'{function.__name__} - {random.randint(10, 20)} минут!'
    return func


@log
def bake():
    pass


if __name__ == '__main__':
    pass
