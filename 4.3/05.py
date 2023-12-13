def result_accumulator(input_func):
    # Накопление результата
    func_result_list = []

    def wrapper(*args, method="accumulate"):
        func_result_list.append(input_func(*args))
        if method == "drop":
            temp = func_result_list.copy()
            func_result_list.clear()
            return temp
        elif method == "accumulate":
            return None
        else:
            raise ValueError

    return wrapper
