def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def merge(a_tuple, b_tuple):
    # Слияние

    return tuple(bubbleSort(list(a_tuple + b_tuple)))
