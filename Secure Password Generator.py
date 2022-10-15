"""
Генератор безопасных паролей

Описание проекта:
программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то,
какие символы требуется в него включить, а какие исключить.

Составляющие проекта:
 - Целые числа (тип int);
 - Переменные;
 - Ввод / вывод данных (функции input() и print());
 - Условный оператор (if/elif/else);
 - Цикл for и while;
 - Словари;
 - Написание пользовательских функций;
 - Работа с модулем random для генерации случайных чисел.

Примечание 1.
Добавлена проверка корректности введенных пользователем данных на этапе ввода длины пароля,
а также на этапе добавления типа символов.
"""

import random

chars = ''

password_filling = {'digits': '0123456789',
                    'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
                    'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'punctuation': '!#$%&*+-=?@^_'}


def user_inputs(inp):
    if inp in ['да', 'нет']:
        return True
    else:
        return False


print('Добро пожаловать в генератор безопасных паролей!')

length = input('Укажите длину пароля >>> ')

while length.isdigit() is not True or int(length) <= 0:
    if length.isdigit() is not True:
        print('Вы указали не число.')
    elif int(length) <= 0:
        print('Длина пароля не может быть равна нулю или быть отрицательной.')

    length = input('Укажите корректную длину пароля >>> ')

length = int(length)

questions = ['Включать ли цифры? (да / нет) >>> ',
             'Включать ли маленькие буквы? (да / нет) >>> ',
             'Включать ли большие буквы? (да / нет) >>> ',
             'Включать ли символы? (да / нет) >>> ']

include_digits = None
include_small_letters = None
include_big_letters = None
include_symbols = None

what_to_include = [include_digits, include_small_letters, include_big_letters, include_symbols]

for i in range(len(what_to_include)):
    user_input = input(f'{questions[i]}')

    while user_inputs(user_input) is not True:
        print('Вы ввели что-то не то.')
        user_input = input(f'{questions[i]}')

    what_to_include[i] = user_input

counter = 0

for i in enumerate(what_to_include):
    val = list(password_filling.values())

    if i[1] == 'да':
        chars += val[i[0]]
        counter += 1


def generate_password(ch, ln):
    new_password = []
    for ii in range(ln):
        new_password.append(random.choice(ch))

    random.shuffle(new_password)
    return ''.join(new_password)


if counter == 0:
    print('Ваш пароль пустой.')
elif counter > length:
    print('Длина вашего пароля меньше количества типов символов.')
else:
    print(f'Ваш пароль: {generate_password(chars, length)}')
