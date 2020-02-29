import random

list_random = [11, 9]
for e in range(10):
    n = round(random.random() * 50)
    list_random.append(n)
print(list_random)
result = []
for sq in list_random:
    if sq >= 0:
        root_num = sq ** 0.5
        if root_num == int(root_num):
            result.append(int(root_num))
print(result)

months = ('',
          'January', 'February', 'Mart', 'April', 'May')
days = ('', 'first', 'second', 'third', 'fourth', 'fifth')
date = '04.05.1998'
day, month, year = date.split('.')
day = int(day)
month = int(month)
year = int(year)

print(days[day], months[month], year, 'year')

list_random1 = []
for e in range(random.randint(0, 10)):
    list_random1.append(round(random.randint(-100, 100)))
print(list_random1)

lst = [1, 2, 4, 5, 6, 2, 5, 2, 7, 8, 8]
print(lst)
lst2 = []
lst3 = set(lst)
for e in lst:
    if lst.count(e) == 1:
        lst2.append(e)

for e in lst:
    if lst.count(e) > 1:
        lst.remove(e)
        lst3 = lst

print((lst3))
print(lst2)
