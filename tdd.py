


def list_sort(argument):
    argument.sort()
    list_two = []
    for i in range(len(argument)):
        if i % 2 == 0:
            list_two.append(argument[i])

    return list_two



