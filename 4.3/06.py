def merge_sort(array):
    # Сортировка слиянием
    array_lenght = len(array)
    if array_lenght <= 1:
        return array
    else:
        return merge(
            merge_sort(array[:array_lenght // 2]),
            merge_sort(array[array_lenght // 2:]),
        )


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
