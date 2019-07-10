LORE = 'Игра "Кошмар в лаборатории". Локация - секретная лаборатория, наше время. Главный герой - сотрудник, который заподозрил, что в лаборатории происходят странные дела.'

print()
print(LORE)
print()
print('Введите имя героя: ')
name = input()

while True:
    print('Кто ваш герой (солдат или ученый)?')
    hero = input()
    if hero == 'солдат':
        HP = 30
        DMG = 20
        break
    elif hero == 'ученый':
        HP = 15
        DMG = 10
        break


print()
print("Приветствую, тебя, {} {}! Удачи в нелегком деле спасения мира!".format(hero, name))

print()

while True:
    print('Список доступных команд: exit (выход из игры), stats (вывод информации о герое), start (начать игру)')
    action = input()
    if action == 'exit':
        print('Пока!')
        exit()
    elif action == 'stats':
        dash = '-' * 40
        print(dash)
        print('{:<10s}{:>4s}{:>12s}{:>12s}'.format('Имя', 'Класс', 'HP', 'Урон'))
        print('{:<10s}{:>4s}{:>11}{:>12}'.format(name, hero, HP, DMG))
        print(dash)
        print()
    elif action == 'start':
        break
    else:
        print('Недопустимая команда!')
        print()

while True:
    print()
    print('Перед вами стоит монстр, он скалит зубы и рычит! Сколько здоровья дадим этому засранцу (целое число)?')
    enemy_hp = (input())
    if enemy_hp.isdigit():
        enemy_hp = int(enemy_hp)
        break
    else:
        print()
        print('Целое число, ау!')

while enemy_hp > 0:
    print()
    print('У врага осталось {} пунктов здоровья, а у героя - {}.'.format(enemy_hp, HP))
    print()
    print('Бьем?')
    action = input()
    if action == 'да':
        enemy_hp -= DMG


print()
print('Поздравляем! Вы победили! Мир спасен!')
