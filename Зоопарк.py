zoo_list = ['жираф', 'зебра', 'собака', 'обезьяна', 'крокодил']


def calculation(position):
    """
    Рассчет позиции для каждого животного.
    Основная логика построена на проверке длины списка.
    Обработаны крайние значения.
    """

    lenght_zoo = len(zoo_list)
    if lenght_zoo == 0:
        return 'Список пуст'
    elif (position+1) > lenght_zoo:
        return 'Значение лежит вне списка!'
    elif lenght_zoo == 2:
        return zoo_list
    elif position == 0:
        return (f'Соседи для {zoo_list[position]},'
                f'справа {zoo_list[position+1]}, '
                f'слева {zoo_list[-1]}')
    elif (position+1) == lenght_zoo:
        return (f'Соседи для {zoo_list[position]},'
                f'справа {zoo_list[0]}, '
                f'слева {zoo_list[position-1]}')
    else:
        return (f'Соседи для {zoo_list[position]},'
                f'справа {zoo_list[position+1]}, '
                f'слева {zoo_list[position-1]}')


def main(value):
    """
    Основная логика программы.
    """

    return print(calculation(value))


if '__main__' == __name__:
    main(5)
