import itertools


def main():
    # Таблица истинности

    expression = input()

    variable_name_alphabet = [chr(i) for i in range(97, 123)]
    variable_name_list = []
    for variable_name in variable_name_alphabet:
        if variable_name in expression.split():
            variable_name_list += [variable_name]

    print(*variable_name_list, "f")

    value_matrix = itertools.product(range(0, 2), repeat=len(variable_name_list))
    for value_tuple in value_matrix:
        exec(", ".join(variable_name_list) + "= value_tuple")
        print(*value_tuple, int(eval(expression)))


if __name__ == "__main__":
    main()
