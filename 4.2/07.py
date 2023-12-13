number_list = []


def enter_results(*args):
    # В эфире рубрика «Эксперименты»

    global number_list
    number_list += list(args)


def get_sum():
    left_number_sum = sum(number_list[::2])
    right_number_sum = sum(number_list[1::2])
    return round(left_number_sum, 2), round(right_number_sum, 2)


def get_average():
    left_average_number = 2 * get_sum()[0] / len(number_list)
    right_average_number = 2 * get_sum()[1] / len(number_list)
    return round(left_average_number, 2), round(right_average_number, 2)
