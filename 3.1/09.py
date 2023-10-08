def main():
    # Без комментариев
    
    line = "Hello, @dexfrost89"
    while line != "":
        line = input()
        comment_start_index = line.find("# ")
        if comment_start_index == -1:
            print(line)
        elif comment_start_index == 0:
            pass
        else:
            print(line[:comment_start_index])


if __name__ == "__main__":
    main()
