import random


fruits = ['apple', 'kiwi', 'watermelon', 'melon']
x = 1
for fruit in fruits:
    print('{}{}'.format(x, '.'), fruit.rjust(10))
    x += 1
fruits = ['apple', 'kiwi', 'watermelon', 'melon','mashmallonfsassasa']
right_offset = len(max(fruits, key=len))
for i, f in enumerate(fruits, start=1):
    print('{}. {}'.format(i, f.rjust(right_offset)))


list1 = [1, 2, 3, 4, 56, 221, 21]
list2 = [9, 8, 21, 221, 56]
for e in list1:
    if not e in list2:
        print(e)
list12 = [e for e in list1 if not e in list2]
print(list12)
print(set(list1) - set(list2))

a = []
for i in range(10):
    n = round(random.random() * 50)
    a.append(n)
print(a)
b = []
for e in a:
    if e % 2 == 0:
        b.append(e / 4)
    else:
        b.append(e * 2)

print(b)