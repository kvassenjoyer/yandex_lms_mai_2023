def main():
    # Рациональная считалочка
    
    start, finish, step = map(float, input().split())
    
    current = start
    while (current <= finish):
        print("%.2f" % current)
        current += step


if __name__ == "__main__":
    main()
