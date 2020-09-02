import random
import os


def new_file():
    new_names = names
    name_file = os.path.isfile('names.txt')
    if name_file:
        req_file = open('names.txt', 'r')
        if len(list(req_file)) == len(names):
            n = 18
            nfirstlines = []
            with open("names.txt") as f, open("namestmp.txt", "w") as out:
                for x in range(n):
                    nfirstlines.append(next(f))
                for line in f:
                    out.write(line)
            os.remove("names.txt")
            os.rename("namestmp.txt", "names.txt")
        f = open('names.txt', 'r')
        for item in f:
            item = item.replace('\n', '')
            new_names.remove(item)
    return new_names


def check_file():
    name = random.choice(new_file())
    file = open('names.txt', 'a')
    file.write(f'{name}\n')
    file.close()
    return name


if __name__ == '__main__':
    names = ['Iron Man', 'Captain America', 'Hulk', 'Thor Odinson', 'Black Widow', 'Hawkeye', 'War Machine',
             'Ant-Man', 'Doctor Strange', 'Black Panther', 'Captain Marvel', 'Spider-Man', 'Nebula', 'Gamora',
             'Wasp', 'Jarvis', 'Groot', 'Rocket', 'Thanos', 'Nick Fury', 'Friday']
    print(check_file())
