import os
import shutil
import sys


def init():
    os.mkdir('.zeon_fs')


_, *args = sys.argv

print(*args)
xar = args[0]
try:
    xar2 = args[1]
except:
    pass


def dir():
    print("Текущая деректория:", os.getcwd())


def delete(command):
    os.remove(command)


def create(command):
    os.mkdir(command)
    dir()


def all_file():
    print("Все папки и файлы:", os.listdir())


def fine_file(command):
    return os.chdir(command)




def copy(command, command2):
    shutil.copy2(fr'{command}', fr'{command2}')  # Копирование файла


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
    try:
        init()
    except:
        pass

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
