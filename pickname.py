import random
import os


def check_file():
    name = random.choice(new_names)
    file = open('names.txt', 'a')
    file.write(f'{name}\n')
    file.close()
    return name


if __name__ == '__main__':
    names = ['Iron Man', 'Captain America', 'Hulk', 'Thor Odinson', 'Black Widow', 'Hawkeye', 'War Machine',
             'Ant-Man', 'Doctor Strange', 'Black Panther', 'Captain Marvel', 'Spider-Man', 'Nebula', 'Gamora',
             'Wasp', 'Jarvis', 'Groot', 'Rocket', 'Thanos', 'Nick Fury', 'Friday']
    new_names = names
    name_file = os.path.isfile('names.txt')
    if name_file:
        fil = open('names.txt', 'r')
        for item in fil:
            item = item.replace('\n', '')
            new_names.remove(item)
        if len(list(fil)) == len(names):
            os.remove('names.txt')
            print('File has been removed after choosing all team members. Re-run the script for a fresh start.')
            exit(0)
    print(check_file())
