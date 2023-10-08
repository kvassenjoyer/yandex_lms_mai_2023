def main():
    # На старт! Внимание! Марш!
    
    n = int(input())
    base_countdown = 3
    for racer_index in range(n):
        for seconds in range(base_countdown + racer_index, 0, -1):
            print(f"До старта {seconds} секунд(ы)")
        print(f"Старт {racer_index+1}!!!")


if __name__ == "__main__":
    main()
