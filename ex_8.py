name = input('Здравствуйте! Как Вас зовут? ')
print(f'У Вас очень красивое имя, {name}! Меня зовут Марк)')
age = int(input('Сколько Вам лет? '))
if age < 84:
    print(f'Ого, {name}! Я старше Вас на {84 - age} лет')
else:
    print(f'Ого, {name}! Я младше Вас на {age - 84} лет')
hobby = input('Вам нравится готовить? ')
if hobby.lower() == 'да':
    print('Ух ты! Это здорово ;)')
else:
    print('Жаль(((')
