names  = ['Ivan', 'Kira', 'Leonid', 'Alex', 'Nina','Viktor']
salary = [9000, 7000, 15000, 9000, 10000, 510000]

dict_sal = (dict(zip(names, salary)))

MAX_SALARY = 500000
TAX = 13

f = open('salary.txt', 'w+', encoding='UTF-8')

for key, value in dict_sal.items():
    if value <= MAX_SALARY:
        f.write('{} - {}\n'.format(key, value))
f.seek(0)
# print(f.read())

for line in f:
    names, salary = line.split(' - ')
    tax = int(salary)/100 * TAX
    salary_after_tax = int(salary) - int(tax)
    print('{}, your salary is {}, after tax'.format(names, salary_after_tax))
f.close()

name = ['Vasya', 'Petro', 'Yuriy']
salary = [20000, 500001, 25000]
vedomost = dict(zip(name, salary))

MAX_SALATY = 500000
TAX = 0.13
with open('salary2.txt', 'w+', encoding='UTF-8') as f:
    for n, s in vedomost.items():
        f.write(f'{n} - {s}\n')
    f.seek(0)
    for line in f:
        nam, salo = line.split('-')
        if int(salo) <= MAX_SALATY:
            tax = int(salo) * TAX
            salary_after_tax = int(salo) - int(tax)
            print(nam, salary_after_tax)