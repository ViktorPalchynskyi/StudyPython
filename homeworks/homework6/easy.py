from abc import *
import random


class Car(metaclass=ABCMeta):

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    @abstractmethod
    def go(self):
        print('The car is going')

    @abstractmethod
    def stop(self):
        print('The car stopped')


    def turn(self, direction):
        print(f'The car turned {direction}')


class TownCar(Car):

    def __init__(self, speed, color, name, comfort):
        super().__init__(speed, color, name)
        self.comfort = comfort

    def go(self):
        print('The town car is going')

    def stop(self):
        print('The town car stopped smooth')




class WorkCar(Car):
    def __init__(self, speed, color, name, capacity):
        super().__init__(speed, color, name)
        self.capacity = capacity

    def go(self):
        print('The working car is going to take a trash')

    def stop(self):
        print('The working car stopped to take a trash')




class PoliceCar(Car):
    def __init__(self, speed, color, name, blinkers, ):
        super().__init__(speed, color, name)
        self.blinkers = blinkers

    def go(self):
        if self.blinkers == True:
            print('The police car turned on a blinkers and go')
        else:
            print('The police car go without blinkers')

    def stop(self):
        print('The police car stopped to take criminal\'s')




tc = TownCar(150, 'red', 'Nissan', 'class S')
wc = WorkCar(120, 'white', 'TrashCar', 400)
pc = PoliceCar(160, 'black and white', 'pegoun',  False)
cars = [tc, wc, pc]
direction = ('left', 'right')
for car in cars:
    car.go()
    car.stop()
    car.turn(random.choice(direction))
