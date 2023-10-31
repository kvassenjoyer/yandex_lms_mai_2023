import itertools


def main():
    # А есть ещё варианты?

    n = 3
    card_suit_case_dict = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "черви": "червей",
    }
    card_suit_list = ["бубен", "пик", "треф", "червей"]
    card_value_list = sorted(
        ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    )   # why sorted

    necessary_card_suit = input()
    forbidden_card_value = input()
    previous_layout = input()

    necessary_card_suit = card_suit_case_dict[necessary_card_suit]
    card_value_list.remove(forbidden_card_value)

    card_layout_tuple = tuple(
        itertools.permutations(itertools.product(card_value_list, card_suit_list), r=3)
    )
        
    card_layout_tuple = (
        ", ".join(" ".join(card_tuple) for card_tuple in sorted(card_layout)) for card_layout in card_layout_tuple
    )   # why sorted
    
    card_layout_list = []
    for card_layout in sorted(set(card_layout_tuple)):  # why sorted
        if necessary_card_suit in card_layout:
            card_layout_list += [card_layout]
    
    result_index = card_layout_list.index(previous_layout) + 1
    print(card_layout_list[result_index])


if __name__ == "__main__":
    main()
