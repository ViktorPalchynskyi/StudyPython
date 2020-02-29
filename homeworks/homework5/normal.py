from homeworks.homework5 import mk_dir, rm_dir, list_dir
import os


def change_dir(folder):
    try:
        os.chdir(folder)
        print('Successfully moved to the folder')
    except FileNotFoundError:
        print('You can\'t move to the folder, it\'s not exist')


do = {
    1: change_dir,
    2: list_dir,
    3: rm_dir,
    4: mk_dir
}

while True:
    choice = input('Choose one of section from the list:\n'
    '===================================================\n'
    '1. Go to a folder\n'
    '2. Check a folder content\n'
    '3. Remove a folder\n'
    '4. Create a folder\n'
    '5. Exit\n\n')
    try:
        if len(choice.split()) == 2:
            choice, folder_name = choice.split()
            choice = int(choice)
            if do.get(choice):
                do[choice](folder_name)
        else:
            choice = int(choice)
            if choice == 5:
                break
            elif do.get(choice):
                print(do[choice]())
    except ValueError:
        print('Error, you type wrong data!')
