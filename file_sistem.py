import os
import shutil
import sys


def init(fs_path):
    if os.path.exists(fs_path) == False:  # Проверка существует ли такой файл
        os.mkdir(fs_path)
        return fs_path


_, *args = sys.argv

xar = args[0]
try:
    xar2 = args[1]
except:
    pass


def dir():
    print("Текущая деректория:", os.getcwd())


def delete(command):
    os.remove(command)
    return os.path.exists(command)


def create(command):
    os.mkdir(command)
    dir()
    return command


def all_file():
    print("Все папки и файлы:", os.listdir())
    return type(os.listdir())


def fine_file(command):
    return os.chdir(command)


def copy(command, command2):
    shutil.copy2(fr'{command}', fr'{command2}')  # Копирование файла

    return fr'{command2}\{command}'


commands = {
    'dir': dir,
    'create': create,
    'fine_file': fine_file,
    'copy': copy,
    'all_file': all_file,
    'delete': delete

}

for key in commands:
    if xar == key:
        try:

            commands[key](xar2)
        except:
            pass
        dir()
    else:
        pass

if __name__ == '__main__':
    init()

if xar in commands:
    print('Hi')
    # print(sys.path)
    try:
        commands[xar]()
    except:
        pass

    try:
        commands[key](xar2, args[2])
    except:
        pass
