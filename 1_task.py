# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
from os import mkdir, path, rmdir


def mk_parents_dir(directory):
    for i in range(1, 9):
        mkdir(path.join(directory, 'dir_{}'.format(i)))


def delete_dir(directory):
    for i in range(1, 9):
        rmdir(path.join(directory, 'dir_{}'.format(i)))


if __name__ == "__main__":
    from os import getcwd
    delete_dir(getcwd())
