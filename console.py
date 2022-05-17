import os

# inp = input()
inper = input().split()
print(inper[0])

if len(inper) == 2:
    twoind = inper[1]

inp = inper[0]


###########################
def tek_dir():
    print("Текущая деректория:", os.getcwd())


def create(a):
    os.mkdir(a)
    tek_dir()


def Perechod(a):
    os.chdir(a)
    tek_dir()


def Back():
    # вернуться в предыдущую директорию
    os.chdir("..")
    tek_dir()


def delete(a):
    os.rmdir(a)
    tek_dir()


def Read_one(a):
    # вывести некоторые данные о файле
    print(os.stat(a))


def all_file():
    print("Все папки и файлы:", os.listdir())


if "dir" == inp:
    tek_dir()

elif "create " == inp:
    create(twoind)

elif 'Perechod' == inp:
    Perechod(twoind)

elif 'back' == inp:
    Back()
    tek_dir()

elif 'files' == inp:

    all_file()

elif 'delete' == inp:
    delete(twoind)


elif 'onefile' == inp:
    Read_one(twoind)
