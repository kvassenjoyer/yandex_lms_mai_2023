def main():
    # Очистка данных
    
    line = "Hello, @dexfrost89"
    while line != "":
        line = input()
        if line.endswith("@@@"):
            pass
        elif line.startswith("##"):
            print(line[2:])
        else:
            print(line)


if __name__ == "__main__":
    main()
