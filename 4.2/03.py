def gcd(*args):
    # Функциональный нод 2.0
    
    number_list = list(args)

    while len(number_list) > 1:
        left = number_list[0]
        right = number_list[1]

        while left != right:
            if left > right:
                left -= right
            else:
                right -= left

        number_list.pop(0)
        number_list[0] = left

    return number_list[0]
