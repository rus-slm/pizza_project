from pizza import *
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    print(f'Готовим Вашу пиццу {pizza} за 10 минут')
    if delivery:
        print('Доставим Вашу пиццу за 40 минут')


@cli.command()
def menu():
    """Выводит меню"""
    print(f' - 🧀 The cheesest Margherita in your life: {Margherita().dict()}')
    print(f' - 🌶 The hottest Pepperoni in the world: {Pepperoni().dict()}')
    print(f' - 🍍 The sweetest Hawaiian in these days: {Hawaiian().dict()}')
    print(f' - 🌱 The healthy Spinach in your life: {Spinach().dict()}')


if __name__ == '__main__':
    cli()
