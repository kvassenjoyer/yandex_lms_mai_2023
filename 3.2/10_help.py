def main():
    """
    Выводит стинтаксически правильное объявление словаря
    по таблице из описания задания 
    """

    line = "default"
    my_dict = {}

    while line != "":
        line = input()
        if " — " in line:
            key, value = line.split(" — ")
            my_dict[key] = value

    my_dict['Ъ'] = ''
    my_dict['Ь'] = ''

    print(my_dict)


if __name__ == "__main__":
    main()
