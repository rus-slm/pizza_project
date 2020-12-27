from pizza import *
import pytest


@pytest.mark.parametrize('s,exp', [(Hawaiian(), 'tomato_sause, mozzarella, chiken, pineapples'),
                                   (Margherita(), 'tomato_sause, mozzarella, tomatoes'),
                                   (Spinach(), 'tomato_sause, mozzarella, spinach'),
                                   (Pepperoni(), 'tomato_sause, mozzarella, pepperoni')])
def test_recipes(s, exp):
    """Тестируем рецепты"""
    assert s.dict() == exp


random.seed(10)


def test_bake():
    """Тестируем декоратор и функцию bake"""
    assert bake() == 'bake - 19 минут!'


@pytest.mark.parametrize('s,exp', [(Hawaiian('S'), 'L'),
                                   (Pepperoni('XL'), 'XL'),
                                   (Spinach('L'), 'L')])
def test_size(s, exp):
    """Тестируем размеры"""
    assert s.size == exp
