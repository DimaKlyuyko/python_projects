"""
Числовая угадайка

Описание проекта:
программа генерирует случайное число в диапазоне от 10 до 100 и просит пользователя угадать это число.
Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Ваше число больше загаданного,
попробуйте еще разок.'. Если догадка меньше случайного числа, то программа должна вывести сообщение
'Ваше число меньше загаданного, попробуйте еще разок.'.
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.

Составляющие проекта:
 - Целые числа (тип int);
 - Переменные;
 - Ввод / вывод данных (функции input() и print());
 - Условный оператор (if/elif/else);
 - Цикл while;
 - Бесконечный цикл;
 - Операторы break, continue;
 - Работа с модулем random для генерации случайных чисел.

Примечание 1.
Добавлена возможность подсчета попыток, сделанных пользователем.
Когда число отгадано, показывает количество попыток.

Примечание 2.
Добавлена возможность генерации нового числа (повторная игра), после того, как пользователь угадал число.
"""

from random import *

n = randint(1, 100)
counter = 0
new_game = True

print('Добро пожаловать в числовую угадайку!')


def is_valid(ui):
    if ui in [str(i) for i in range(1, 101)]:
        return True
    else:
        return False


def continue_validation(ing):
    if ing in ['да', 'нет']:
        return True
    else:
        return False


while new_game is True:
    user_input = input('Введите число от 1 до 100 >>> ')

    if is_valid(user_input) is not True:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        user_input = int(user_input)

    if user_input < n:
        print('Ваше число меньше загаданного, попробуйте еще разок.')
        counter += 1
    elif user_input > n:
        print('Ваше число больше загаданного, попробуйте еще разок.')
        counter += 1
    else:
        print(f'Вы угадали, поздравляем! Загаданное число = {n}.')
        print(f'Количество попыток = {counter}.')

        is_new_game = input('Хотите сыграть ещё раз? (да / нет) >>> ')

        while continue_validation(is_new_game) is not True:
            print('Вы ввели что-то не то.')
            is_new_game = input('Хотите сыграть ещё раз? (да / нет) >>> ')
            continue

        if is_new_game == 'да':
            n = randint(1, 100)
            counter = 0
            continue
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся.')
