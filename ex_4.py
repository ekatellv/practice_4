print('Вы поедете на бал?')
answer = input('Ответ: ')
if answer.lower() not in ('да', 'нет'):
    print('Верно')
else:
    print('Неверно')
