def main():
    # Список победителей

    # Можно использовать вложенные списки, словари, класс runner и OrderedDict из collections
    name_list = ["Петя", "Вася", "Толя"]
    runner_dict = {}
    for i in range(len(name_list)):
        runner_dict[name_list[i]] = int(input())

    runner_dict = dict(sorted(runner_dict.items(), key=lambda item: -1 * item[1]))

    for position, runner_name in enumerate(runner_dict.keys()):
        print(f"{position+1}. {runner_name}")


if __name__ == "__main__":
    main()
