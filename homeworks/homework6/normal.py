from abc import *
import random

class Person:

    def __init__(self, name, health=100, damage=20, armor=1.2):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__armor = armor
        self.__lvl = 1
        print(f'(The {self.__lvl} lvl person {self.__name} was created)')

    def get_health(self):
        return self.__health

    def get_armor(self):
        return self.__armor

    def get_damage(self):
        return self.__damage

    def get_lvl(self):
        return self.__lvl

    def __set_health(self, value):
        if self.__health > 0:
            self.__health = value
        else:
            print('Hp can\'t be negative')

    def hit(self, damage):
        self.__set_health(self.__health - damage)

    def __calculate_damage(self, enemy):
        return self.__damage / enemy.get_armor()

    def attack(self, enemy):

        damage = self.__calculate_damage(enemy)
        enemy.hit(damage)

        print(f'{self.__name} damage {enemy.__name}, {enemy.__name} have {round(enemy.get_health())} hp')


class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)
        self.__experience = 1
        self.__ex_to_next_lvl = 100

        print(f'The player {name} was created')
        print(f'Player {name} have {health} hp and {damage} damage')

    def get_experience(self):
        return self.__experience

    def __is_next_level(self):
        if self.__experience >= self.__ex_to_next_lvl:
            self.__lvl += 1
            self.__ex_to_next_lvl *= 2

    def increase_experience(self, value):
        if value > 0:
            self.__experience += value
            self.__is_next_level()


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)
        # self.__lvl = lvl
        # self.__health *= lvl
        # self.__armor *= lvl
        # self.__damage *= lvl
        print(f'The enemy {name} was created')
        print(f'Enemy {name} have {health} hp and {damage} damage')


class Game():

    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy



    def start(self):
        print('A fight has began!')
        random_list = [self.__player, self.__enemy]
        attacker = random.choice(random_list)
        while self.__player.get_health() > 0 and self.__enemy.get_health() > 0:
            if attacker == self.__player:
                self.__player.attack(self.__enemy)
                attacker = self.__enemy
            else:
                self.__enemy.attack(self.__player)
                attacker = self.__player

        if self.__player.get_health() > 0:
            print('Player won')
        else:
            print('Enemy won')


p2 = Person('Kiss')
p1 = Player('Vic', random.randint(100, 150), random.randint(40, 50), 1.2)
e1 = Enemy('Tor', random.randint(100, 150), random.randint(40, 50), 1.2)
a1 = Game(p1, e1)

a1.start()
