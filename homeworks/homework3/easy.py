from random import random

list1 = [1, 2, 3, 4, 66, 88, 12]
list2 = ['I', 'am', 'your', 'father', 'Luk', 'lala', 'Jaja', '223']
list3 = []
for n in range(1, 10):
    n = round(random() * 1000)
    list3.append(n)
print(list3)
print(dict(zip(list1, list2)))
print(list(filter(lambda x: x > 100, list3)))


def identification(name, age, city):
    return '%s, %s years old, lives in %s.' % (name, age, city)


name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter your city: ')
print(identification(name, age, city))


def my_mult(a, b, c):
    return max(a, b, c)


print(my_mult(55, 1, 76))
