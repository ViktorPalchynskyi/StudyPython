import re

pattern1 = (r'\b[A-Z][a-z]+')
pattern2 = (r'[a-z_\d]+@\w+\.[ru|org|com]+')
some = 'Aasljfd alsjfdl Fkaljsf alskdfl kasdfFsklaj ffSFjf'
result = re.findall(pattern1, some)
result1 = re.match(pattern1, some)


name = input('Your name: ')
surname = input('Your surname: ')
email = input('Your email: ')
while True:
    if re.match(pattern1, name):
        if re.match(pattern1, surname):
            if re.match(pattern2, email):
                print('Everything is correct!')
                break
            else:
                print('Name and surname is write, but email is wrong!')
                email = input('Type your email again, please: ')


        else:
            print('Your name is right, but surname is wrong!')
            surname = input('Type your surname again: ')
    else:
        name = input('Type your name again: ')



some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern1 = r'\b\.\.+'
if re.findall(pattern1, some_str):
    print('There are more than two dots in a row')
else:
    print('There are\'t more than two dots in a row')