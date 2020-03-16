import random

player1 = input("Player 1 name: ")
player2 = input("Player 2 name: ")

number_of_sticks = 10
player_turn = 1


# rand_list = [player1, player2]
# last_player = random.choice(rand_list)
#
# while number_of_sticks > 0:
#
#     print(f'It\'s {last_player} turn to pick')
#     print(f'There are {number_of_sticks} left')
#     num = int(input('How many wood\'s do you want to get?\n'))
#
#
#     if num == 0 or num > 3:
#         print('You pick the wrong number, you need the number between 1 and 3')
#         continue
#
#     if num > number_of_sticks:
#         print(f"You can't get more thant {number_of_sticks} woods")
#         continue
#
#     if last_player == player1:
#         print(f'{player1} have got {num} wood\'s')
#         number_of_sticks -= num
#         last_player = player2
#
#     elif last_player == player2:
#         print(f'{player2} have got {num} wood\'s')
#         number_of_sticks -= num
#         last_player = player1
#
#
#
#     if number_of_sticks == 0 and last_player == player1:
#         print(f'{player1} won!')
#     elif number_of_sticks == 0 and last_player == player2:
#         print(f'{player2} won!')


def can_take(sticks_taken, remaining_stick):
    return 1 <= sticks_taken <= 3 and sticks_taken <= remaining_stick


def switch_player_turn(turn):
    return 1 if turn == 2 else 2


def end_of_game(sticks):
    return sticks <= 0


while not end_of_game(number_of_sticks):
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())

    if not can_take(taken, number_of_sticks):
        if taken > number_of_sticks:
            print('You tried to take more than on the table.')
        else:
            print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks.')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \n Player {player_turn} has lost')
        break

    player_turn = switch_player_turn(player_turn)
