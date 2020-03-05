import random

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")

WOODS = 10

rand_list = [player1, player2]
last_player = random.choice(rand_list)

while WOODS > 0:

    print(f'It\'s {last_player} turn to pick')
    print(f'There are {WOODS} left')
    num = int(input('How many wood\'s do you want to get?\n'))


    if num == 0 or num > 3:
        print('You pick the wrong number, you need the number between 1 and 3')
        continue

    if num > WOODS:
        print(f"You can't get more thant {WOODS} woods")
        continue

    if last_player == player1:
        print(f'{player1} have got {num} wood\'s')
        WOODS -= num
        last_player = player2

    elif last_player == player2:
        print(f'{player2} have got {num} wood\'s')
        WOODS -= num
        last_player = player1



    if WOODS == 0 and last_player == player1:
        print(f'{player1} won!')
    elif WOODS == 0 and last_player == player2:
        print(f'{player2} won!')
