LORE = 'Игра "Кошмар в лаборатории". Локация - секретная лаборатория, наше время. Главный герой - сотрудник, который заподозрил, что в лаборатории происходят странные дела.'

print()
print(LORE)
print()

roles = {'soldier': {'MAX_HP':30, 'CUR_HP':30, 'DMG':20, 'MEDKIT':2}, 'scientist': {'MAX_HP':15, 'CUR_HP': 15, 'DMG':10, 'MEDKIT':5}}

commands = ('exit','stats','start','help','train','help')

enemies = [{'Охранник':{'HP':10, 'DMG':5}}, {'Мелкий монстр':{'HP':10, 'DMG':8}}, {'Спецназовец':{'HP':20, 'DMG':10}}, {'Монстр-громила':{'HP':50, 'DMG':14}}]

instructor = {'HP':0}

train_hero = {'DMG':0}

hero_dead = False

artefact = False

print('Введите имя героя: ')
name = input().capitalize()

while True:
    print('Кто ваш герой (солдат или ученый)?')
    hero_input = input()
    if hero_input == 'солдат':
        hero = roles['soldier']
        break
    elif hero == 'ученый':
        hero = roles['scientist']
        break


print()
print("Приветствую, тебя, {} {}! Удачи в нелегком деле спасения мира!".format(hero_input, name))

print()

while True:
    print('Список доступных команд: exit (выход из игры), stats (вывод информации о герое), train (тренировочный бой),start (начать игру), help (снова вывести этот текст)')
    action = input().lower()
    print()
    if action not in commands:
        print('Недопустимая команда!')
        print()
    if action == 'exit':
        print('Пока!')
        exit()
    elif action == 'stats':
        dash = '-' * 40
        print(dash)
        print('{:<10s}{:>4s}{:>12s}{:>12s}'.format('Имя', 'Класс', 'HP', 'Урон'))
        print('{:<10s}{:>4s}{:>11}{:>12}'.format(name, hero_input, hero['CUR_HP'], hero['DMG']))
        print(dash)
        print()

    elif action == 'train':

        while True:
            print()
            print('Сколько пунктов здоровья дадим инструктору (целое число)?')
            instructor['HP'] = (input())
            if instructor['HP'].isdigit():
                instructor['HP'] = int(instructor['HP'])
                break
            else:
                print()
                print('Целое число, ау!')

        while True:
            print()
            print("Насколько силен удар героя?")
            train_hero['DMG'] = int(input())

            if train_hero['DMG'] > instructor['HP']:
                print(
                    "Урон героя не может превышать жизни противника, поэтому мы ограничили урон. Чтоб все по-честному!")
                train_hero['DMG'] = instructor['HP'] / 4
                break
            else:
                break


        while instructor['HP'] > 0:
            print()
            print('У инструктора осталось {} пунктов здоровья, а у героя - {}.'.format(instructor['HP'], hero['CUR_HP']))
            print()
            print('Бьем?')
            action = input()
            if action == 'да':
                instructor['HP'] -= train_hero['DMG']

        print('Поздравляем! Вы показали инструктору кто тут босс!')
        print()

    elif action == 'start':

        for enemy in enemies:
            print()
            print('Перед вами {}, у него {} жизней, наносимый урон - {}'.format(list(enemy.items())[0][0], enemy[list(enemy.items())[0][0]]['HP'], enemy[list(enemy.items())[0][0]]['DMG']))
            while enemy[list(enemy.items())[0][0]]['HP'] > 0:
                print()
                print('удар (урон в размере DMG), защита (-70% к урону противника и контратака силой 50% урона героя) или лечимся (полностью восстанавливаем HP)?')
                command = input()

                if command == 'удар':
                    enemy[list(enemy.items())[0][0]]['HP'] -= hero['DMG']
                    hero['CUR_HP'] -= enemy[list(enemy.items())[0][0]]['DMG']
                    if enemy[list(enemy.items())[0][0]]['HP'] < 0:
                        print('Враг повержен! У героя осталось {} жизней'.format(hero['CUR_HP']))
                        break
                    elif hero['CUR_HP'] < 0:
                        hero_dead = True
                        break
                    else:

                        print()
                        print('У врага осталось {} пунктов здоровья, а у героя: {}.'.format(enemy[list(enemy.items())[0][0]]['HP'], hero['CUR_HP']))


                elif command == 'защита':
                    enemy[list(enemy.items())[0][0]]['HP'] -= hero['DMG'] * 0.5
                    hero['CUR_HP'] -= enemy[list(enemy.items())[0][0]]['DMG'] * 0.7

                    if enemy[list(enemy.items())[0][0]]['HP'] < 0:
                        print('Враг повержен! У героя осталось {} жизней'.format(hero['CUR_HP']))
                        break
                    elif hero['CUR_HP'] < 0:
                        hero_dead = True
                        break
                    else:

                        print()
                        print('У врага осталось {} пунктов здоровья, а у героя: {}.'.format(enemy[list(enemy.items())[0][0]]['HP'], hero['CUR_HP']))

                elif command == 'лечимся':
                    if hero['MEDKIT'] == 0:
                        print("Аптечки закончились! Держитесь там!")
                    else:
                        hero['MEDKIT'] -= 1
                        hero['CUR_HP'] = hero['MAX_HP']
                        print('У героя снова {} жизней, а у монстра - {}'.format(hero['CUR_HP'], enemy[list(enemy.items())[0][0]]['HP']))

                else:
                    print('Недопустимая команда, поэтому герой выполняет команду \'удар\'')
                    enemy[list(enemy.items())[0][0]]['HP'] -= hero['DMG']
                    hero['CUR_HP'] -= enemy[list(enemy.items())[0][0]]['DMG']
                    if enemy[list(enemy.items())[0][0]]['HP'] < 0:
                        print('Враг повержен! У героя осталось {} жизней'.format(hero['CUR_HP']))
                        break
                    elif hero['CUR_HP'] < 0:
                        hero_dead = True
                        break
                    else:

                        print()
                        print('У врага осталось {} пунктов здоровья, а у героя: {}.'.format(
                            enemy[list(enemy.items())[0][0]]['HP'], hero['CUR_HP']))

        if not hero_dead:
            print()
            print('Вы победили всех врагов. Потрясающе!')
            break
        else:
            print()
            print("Вы погибли! В следующий раз старайтесь лучше!")
            break

print()
print('Game Over')



