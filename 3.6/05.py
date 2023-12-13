import json
import sys


def main():
    # Алфавитная статистика

    data = {}
    for word in sys.stdin:
        if word.endswith("\n"):
            word = word[:-1]
        word = word.lower()
        for i in range(1, len(word), 2):
            word_key = word[i]
            if word_key not in data.keys():
                data[word_key] = [word]
            elif word not in data[word_key]:
                data[word_key] += [word]

    for key in data.keys():
        data[key].sort()

    out_file = open("result.json", "w")
    
    json.dump(data, out_file, indent=6)

    out_file.close()


if __name__ == "__main__":
    main()
