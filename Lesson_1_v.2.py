LORE = 'Игра "Кошмар в лаборатории". Локация - секретная лаборатория, наше время. Главный герой - сотрудник, который заподозрил, что в лаборатории происходят странные дела.'
BEGIN = 'В ходе работы главный герой видит, что эксперименты в лаборатории привели к появлению опасных монстров. Герой решает сделать все, чтобы остановить эксперименты и уничтожить источник опасности.'
FINAL = 'Мир спасен! Вы молодец!'

print()
print(LORE)
print()
print(BEGIN)
print()
print('Введите имя героя: ')
name = input()

while True:
    print('Кто ваш герой (солдат или ученый)?')
    hero = input()
    if hero == 'солдат':
        HP = 30
        DMG = 20
        ARMOR = 20
        STAMINA = 30
        break
    elif hero == 'ученый':
        HP = 15
        DMG = 10
        ARMOR = 10
        STAMINA = 15
        break
    else:
        print("солдат или ученый, других вариантов нет!")
        print()


print()
print("Приветствую, тебя, {} {}! Удачи в нелегком деле спасения мира!".format(hero, name))

print()

while True:
    print('Список доступных команд: help (вывод этой подсказки), exit (выход из игры), stats (вывод информации о герое), train (тренировочный бой), history (еще раз узнать что же тут происходит)')
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
    elif action == 'train':
        break
    elif action == 'help':
        continue
    elif action == 'history':
        print(LORE)
        print()
    else:
        print('Недопустимая команда!')
        print()


print("Настало время для тренировочного боя! Сколько дадим жизней противнику?")
hp_enemy = int(input())
print()
print("Насколько силен удар героя?")
damage = int(input())

if damage > hp_enemy:
    print("Урон героя не может превышать жизни противника, поэтому мы ограничили урон. Чтоб все по-честному!")
    damage = hp_enemy / 4

while hp_enemy > 0:
    print()
    print('У врага осталось {} пунктов здоровья, а у героя - {}.'.format(hp_enemy, HP))
    print()
    print('Бьем?')
    action = input()
    if action == 'да':
        hp_enemy -= damage


print()
print(FINAL)