import random


def generate_person(name, health, damage, armor=1.2):
    return {'name': name, 'health': health, 'damage': damage, 'armor': armor}


def write_person_to_file(person):
    with open(person['name'], 'w', encoding='UTF-8') as f:
        for k, v in person.items():
            f.write(f'{k} {v}\n')


def get_person_by_filename(filename):
    person = {}
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            key, value = line.split()
            if key == 'armor':
                value = float(value)
            elif key != 'name':
                value = int(value)
            person[key] = value
        return person


def calculate_damage(damage, armor):
    return damage / armor


def attack(attacker, defender):
    damage = calculate_damage(attacker['damage'], defender['armor'])
    defender['health'] -= damage
    if defender['health'] < 0:
        defender['health'] = 0

    print(
        '{} damaged {}, {} have {} hp'.format(attacker['name'], defender['name'], defender['name'],
                                              round(defender['health'])))


firs_player_name = input('What is your name?\n')
second_player_name = input('What is your name?\n')

firs_player = generate_person(firs_player_name, random.randint(100, 150), random.randint(40, 50))
second_player = generate_person(second_player_name, random.randint(100, 150), random.randint(40, 50))

print(firs_player)
print(second_player)

write_person_to_file(firs_player)
write_person_to_file(second_player)


def start_game(player1, player2):
    player1 = get_person_by_filename(firs_player_name)
    player2 = get_person_by_filename(second_player_name)
    random_list = [player1, player2]
    attacker = random.choice(random_list)
    while player1['health'] > 0 and player2['health'] > 0:
        if attacker == player1:
            attack(player1, player2)
            attacker = player2
        else:
            attack(player2, player1)
            attacker = player1

    if player1['health'] > 0:
        print('{} won!'.format(player1['name']))
    else:
        print('{} won!'.format(player2['name']))


start_game(firs_player, second_player)