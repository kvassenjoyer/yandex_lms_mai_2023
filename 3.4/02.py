def main():
    # Сборы на прогулку

    first_children_list = input().split(", ")
    second_chidren_list = input().split(", ")

    amount_of_pairs = min(len(first_children_list), len(second_chidren_list))
    
    for i in range(amount_of_pairs):
        print(f"{first_children_list[i]} - {second_chidren_list[i]}")


if __name__ == "__main__":
    main()
