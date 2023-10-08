def main():
    # Легенды велогонок возвращаются: кто быстрее?

    name_list = ["Петя", "Вася", "Толя"]
    runner_dict = {}
    for i in range(len(name_list)):
        runner_dict[name_list[i]] = int(input())

    runner_dict = dict(sorted(runner_dict.items(), key=lambda item: -1 * item[1]))

    first_runner_name = list(runner_dict.keys())[0]
    second_runner_name = list(runner_dict.keys())[1]
    third_runner_name = list(runner_dict.keys())[2]

    step_width = 8
    print(first_runner_name.center(step_width).center(3 * step_width))
    print(second_runner_name.center(step_width).ljust(3 * step_width))
    print(third_runner_name.center(step_width).rjust(3 * step_width))
    print("II".center(step_width) + "I".center(step_width) + "III".center(step_width))


if __name__ == "__main__":
    main()
