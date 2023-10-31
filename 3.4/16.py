import itertools


def main():
    # Расклад таков...

    n = 3
    card_suit_case_dict = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "черви": "червей",
    }
    card_suit_list = ["бубен", "пик", "треф", "червей"]
    card_value_list = (
        ["10"] + list(map(str, range(2, 10))) + ["валет", "дама", "король", "туз"]
    )

    necessary_card_suit = input()
    forbidden_card_value = input()

    necessary_card_suit = card_suit_case_dict[necessary_card_suit]
    card_value_list.remove(forbidden_card_value)

    card_list = []
    for value, suit in itertools.product(card_value_list, card_suit_list):
        card_list += [f"{value} {suit}"]

    card_layout_list = []
    for card_layout in itertools.product(card_list, repeat=n):
        if len(set(card_layout)) == 3:
            card_layout_list += [", ".join(card_layout)]
    
    i = 0
    for card_layout in card_layout_list:
        if necessary_card_suit in card_layout:
            print(card_layout)
            i += 1

        if i == 10:
            break


if __name__ == "__main__":
    main()
