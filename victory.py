right_answer = 0
wrong_answer = 0
greeting = 'Добро пожаловать на викторину'
condition = 'Назовите года писателей!'
"""
start = input('Готовы?(да/нет): ')
while (start == 'да'):
    if start != 'да':
        break
    print('')
    print(greeting)
    print(condition)
    print('')
"""
writers = [
    'А.И. Куприн',
    'Н.В. Гоголь',
    'А.П. Чехов',
    'А.С. Пушкин',
    'М.Ю. Лермонтов',
    'Н.А. Некрасов',
    'И.С. Тургенев',
    'Л.Н. Толстой',
    'И.А. Гончаров',
    'А.Н. Толстой'
]

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одиннадцатое',
    '12': 'двеннадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семьнадцатое',
    '18': 'восемьнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвертое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
    '31': 'тридцать первое',
}

months = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря',
}

import random
result = random.sample(writers, 5)
print(result)
print()


data = '01.01.1876'
day, month, year = data.split('.')
print(days[day], months[month], year, 'года')
"""


    print('Вопрос 1: Какого года рождения А.И. Куприн?')  # Правильный ответ: 1870
    answer1 = int(input('Ответ: '))
    if answer1 == 1870:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 2: Какого года рождения Н.В. Гоголь?')  # Правильный ответ: 1809
    answer2 = int(input('Ответ: '))
    if answer2 == 1809:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 3: Какого года рождения А.П. Чехов?')  # Правильный ответ: 1860
    answer3 = int(input('Ответ: '))
    if answer3 == 1860:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 4: Какого года рождения А.С. Пушкин?')  # Правильный ответ: 1799
    answer4 = int(input('Ответ?: '))
    if answer4 == 1799:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 5: Какого года рождения М.Ю. Лермонтов?')  # Правильный ответ: 1814
    answer5 = int(input('Ответ: '))
    if answer5 == 1814:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 6: Какого года рождения Н.А. Некрасов?')  # Правильный ответ: 1821
    answer6 = int(input('Ответ: '))
    if answer6 == 1821:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 7: Какого года рождения И.С. Тургенев?')  # Правильный ответ: 1818
    answer7 = int(input('Ответ: '))
    if answer7 == 1818:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 8: Какого года рождения Л.Н. Толстой?')  # Правильный ответ: 1828
    answer8 = int(input('Ответ: '))
    if answer8 == 1828:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 9: Какого года рождения И.А. Гончаров?')  # Правильный ответ: 1812
    answer9 = int(input('Ответ: '))
    if answer9 == 1812:
        right_answer += 1
    else:
        wrong_answer += 1
    print('Вопрос 10: Какого года рождения А.Н. Толстой?')  # Правильный ответ: 1883
    answer10 = int(input('Ответ: '))
    if answer10 == 1883:
        right_answer += 1
    else:
        wrong_answer += 1
    print('')
    print('Результаты')
    print('Правильных ответов', right_answer)
    print('Неправильных ответов', wrong_answer)
    print('Процент правильных ответов', right_answer * 100 / 10)
    print('Процент неправильных ответов', wrong_answer * 100 / 10)

    print('')
    restart = input('Сыграть ещё раз?(да/нет): ')
    if restart != 'да':
        break
    start = input('Готовы?(да/нет): ')

print('')
print('Спасибо за участие!')

"""