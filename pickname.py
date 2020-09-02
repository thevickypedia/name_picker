import logging
import os
import random


def new_list():
    new_name_list = name_list
    name_file = os.path.isfile('names.txt')
    if name_file:
        req_file = open('names.txt', 'r')
        file_length = len(list(req_file))
        if file_length == len(name_list):
            # n is the value which has to be removed, currently it is set to 70% of the list
            n = int(len(name_list) - ((30 * file_length) / 100))  # n can also be set to a constant value
            logger.info(f'\tRemoved {n} lines from names.txt as all the names in the list have been picked at least '
                        f'once.')
            # # n can be set 1 if the list is too small and 70% of the list returns 0
            # n = 1 if n == 0 else n
            first_lines = []
            with open("names.txt") as f, open("namestmp.txt", "w") as out:
                for x in range(n):
                    first_lines.append(next(f))
                for line in f:
                    out.write(line)
            os.remove("names.txt")
            os.rename("namestmp.txt", "names.txt")
        f = open('names.txt', 'r')
        for item in f:
            item = item.replace('\n', '')
            new_name_list.remove(item)
    return new_name_list


def check_file():
    name = random.choice(new_list())
    file = open('names.txt', 'a')
    file.write(f'{name}\n')
    file.close()
    return name


if __name__ == '__main__':
    """This main function triggers check_file() function that copies the last 30% of the names to a 
        temp file (which is later deleted) and creates a new file with those 30% of names.
        Pro: A person chosen will NOT end up being the first person chosen when the list is exhausted"""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(' PickName')
    name_list = ['Iron Man', 'Captain America', 'Hulk', 'Thor Odinson', 'Black Widow', 'Hawkeye', 'War Machine',
                 'Ant-Man', 'Doctor Strange', 'Black Panther', 'Captain Marvel', 'Spider-Man', 'Nebula', 'Gamora',
                 'Wasp', 'Jarvis', 'Groot', 'Rocket', 'Thanos', 'Nick Fury', 'Friday']
    print(check_file())
