word_list = []


def add_word(word):
    word_list.append(word)


def get_work():
    # Глобальное сочинение
    
    return ", ".join(word_list) + f". ({len(word_list)})"
