import os
import sys

# Task1
def mk_dir(path):
    try:
        os.mkdir(path)
        print('Directory has been created.')
    except FileExistsError:
        print('Directory has exist already.')
    except PermissionError:
        print('You have no right to create the directory.')


def rm_dir(path):
    try:
        os.removedirs(path)
        print('Directory has been removed.')
    except FileNotFoundError:
        print('Director has\'t found.')
    except PermissionError:
        print('You have no right to create the directory.')


if __name__ == "__main__":
    dir_path = 'dir_{}'
    [mk_dir(dir_path.format(i)) for i in range(1, 10)]
    [rm_dir(dir_path.format(i)) for i in range(1, 10)]
# Task2
def list_dir():
    print([i for i in os.listdir() if os.path.isdir(i)])

# Task3
def create_file_copy():
    filename = sys.argv[0]

    with open(filename, 'rb') as f:
        name, extension = filename.split('.')
        with open(name + '_copy.' + extension, 'wb') as destination_f:
            destination_f.write(f.read())

create_file_copy()

