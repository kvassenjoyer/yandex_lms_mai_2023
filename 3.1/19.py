def main():
    # Польский калькулятор — 2

    expression = input()
    lexem_list = expression.split(" ")
    for i in range(len(lexem_list)):
        if lexem_list[i].isdigit():
            lexem_list[i] = int(lexem_list[i])

    binary_operator_list = ["+", "-", "*", "/"]

    lexem_index = 0
    while len(lexem_list) != 1:
        lexem = lexem_list[lexem_index]
        if lexem in binary_operator_list:
            left_index, right_index = lexem_index - 2, lexem_index - 1
            a, b = lexem_list[left_index], lexem_list[right_index]
            if lexem == binary_operator_list[0]:
                lexem_list[left_index] = a + b
            elif lexem == binary_operator_list[1]:
                lexem_list[left_index] = a - b
            elif lexem == binary_operator_list[2]:
                lexem_list[left_index] = a * b
            elif lexem == binary_operator_list[3]:
                lexem_list[left_index] = a / b

            lexem_list.pop(lexem_index)
            lexem_list.pop(right_index)
            lexem_index -= 2

        lexem_index += 1

    print(lexem_list[0])


if __name__ == "__main__":
    main()
