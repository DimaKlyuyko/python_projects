"""
Шифр Цезаря

Описание проекта:
требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:
 - направление: шифрование или дешифрование;
 - язык алфавита: русский или английский;
 - шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
Примечание 3. Сохраните регистр символов.
Например, текст:
"Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

Составляющие проекта:
 - Целые числа (тип int);
 - Модульная арифметика;
 - Переменные;
 - Ввод / вывод данных (функции input() и print());
 - Условный оператор (if/elif/else);
 - Цикл for/while;
 - Строковые методы;
 - Функции.
"""

# abc - from 97 to 122 (26)
# ABC - from 65 to 90 (26)
# абв - from 1072 to 1103 (32)
# АБВ - from 1040 to 1071 (32)

print('Добро пожаловать в шифратор Цезаря!')

cipher_type = input('Вы ходите зашифровать (1) или дешифровать (0) строку? >>> ')
while cipher_type not in ['1', '0']:
    print('Вы ввели что-то не то')
    cipher_type = input('Вы ходите зашифровать (1) или дешифровать (0) строку? >>> ')

lang = input('Ваша строка на английском (eng) или русском (rus) ? >>> ')
while lang not in ['rus', 'eng']:
    print('Вы ввели что-то не то')
    lang = input('Ваша строка на английском (eng) или русском (rus) ? >>> ')

rot = input('Введите шаг сдвига (int) >>> ')
while rot.isdigit() is not True:
    print('Вы ввели что-то не то')
    rot = input('Введите шаг сдвига (int) >>> ')

rot = int(rot)

finish_string = ''
start_string = input('Введите строку >>> ')


# проверка, что буквы соответствуют алфавиту
def string_check(s, l):
    proverka = ''.join([i.lower() for i in s if i.isalpha() is True])

    if l == 'rus':
        for x in proverka:
            if 1072 <= ord(x) <= 1103:
                continue
            else:
                return False
        return True
    else:
        for x in proverka:
            if 97 <= ord(x) <= 122:
                continue
            else:
                return False
        return True


while string_check(start_string, lang) is not True:
    print('Одна или более букв не соответствуют выбранному алфавиту.')
    start_string = input('Введите строку >>> ')

if cipher_type == '0':
    if lang == 'rus':
        rot = 32 - rot
    else:
        rot = 26 - rot

if lang == 'rus':
    for i in start_string:
        if i.isalpha() is True:
            if i.islower() is True:
                if ord(i) + rot > 1103:
                    finish_string += chr((ord(i) - 32) + rot)
                else:
                    finish_string += chr((ord(i) + rot))
            else:
                if ord(i) + rot > 1071:
                    finish_string += chr((ord(i) - 32) + rot)
                else:
                    finish_string += chr((ord(i) + rot))
        else:
            finish_string += i
elif lang == 'eng':
    for i in start_string:
        if i.isalpha() is True:
            if i.islower() is True:
                if ord(i) + rot > 122:
                    finish_string += chr((ord(i) - 26) + rot)
                else:
                    finish_string += chr((ord(i) + rot))
            else:
                if ord(i) + rot > 90:
                    finish_string += chr((ord(i) - 26) + rot)
                else:
                    finish_string += chr((ord(i) + rot))
        else:
            finish_string += i

print(finish_string)
