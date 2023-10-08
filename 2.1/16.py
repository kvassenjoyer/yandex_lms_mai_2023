def main():
    # Доставка

    a_point = int(input())
    b_point = int(input())
    speed = int(input())
    delivery_time = abs(a_point - b_point) / speed
    print(f"{delivery_time:.2f}")


if __name__ == "__main__":
    main()
