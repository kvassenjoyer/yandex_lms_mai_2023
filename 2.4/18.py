def main():
    # Новогоднее настроение 2.0
    
    max_number = int(input())
    line, line_len_list = '', [0]
    for i in range(1, max_number + 1):
        line += str(i) + ' '
        check_list = [sum(range(j)) for j in range(i + 2)]
        if i in check_list:
            line_len_list += [len(line) - 1]
            line = ''
    line_len_list += [len(line) - 1]
    numbers_in_line = 1
    for i in range(1, max_number + 1):
        check_list = [sum(range(j)) for j in range(i + 2)]
        if i - 1 in check_list:
            if i != 1:
                print(f"{' ' * ((max(line_len_list) - line_len_list[numbers_in_line]) // 2)}{i}", end=' ')
            else:
                print(f"{' ' * ((max(line_len_list) - line_len_list[numbers_in_line]) // 2)}{i}")
            numbers_in_line += 1
        else:
            check_list = [sum(range(j)) for j in range(i + 2)]
            if i in check_list:
                print(i)
            else:
                print(i, end=' ')


if __name__ == "__main__":
    main()
