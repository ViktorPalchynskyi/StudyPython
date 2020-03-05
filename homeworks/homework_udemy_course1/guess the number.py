import random


#
# ran_num = random.randint(1, 50)
# count = 0
# print(ran_num)
# while count < 6:
#     guess_num = int(input('Type your number: '))
#     count += 1
#     if guess_num > ran_num:
#         print(f'The number is lower than {guess_num}')
#     elif guess_num < ran_num:
#         print(f'The number is bigger than {guess_num}')
#     else:
#         print("It's correct number, congratulations!\n"
#               f"You needed {count} try to guess")
#         break
# else:
#     print('You used all attempts')


def ran_num():
    return random.randint(1, 50)


def guess_game():
    count = 0
    ran_num1 = ran_num()
    while count < 6:
        num = int(input('Type your number: '))
        count += 1
        if num > ran_num1:
            print(f'The number is lower than {num}')
        elif num < ran_num1:
            print(f'The number is bigger than {num}')
        else:
            print("It's correct number, congratulations!\n"
                  f"You needed {count} try to guess")
            break
        if count == 6 and num != ran_num1:
            print(f'Sorry, you did\'t make it. My number was {ran_num1}')
            next_game = input('Do you want to play again?\ny or n:\n')
            if next_game == 'y':
                count = 0
                ran_num1 = ran_num()
            else:
                print('Goodbye, my friend!')
                break




guess_game()
