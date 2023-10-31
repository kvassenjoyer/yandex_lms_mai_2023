def main():
    # Колода карт

    card_suit_list = ["пик", "треф", "бубен", "червей"]
    card_value_list = list(range(2, 11)) + ["валет", "дама", "король", "туз"]

    forbidden_card_suit = input()
    card_suit_list.remove(forbidden_card_suit)

    for card_value in card_value_list:
        for card_suit in card_suit_list:
            print(card_value, card_suit)


if __name__ == "__main__":
    main()
