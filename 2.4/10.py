def main():
    # Мы делили апельсин
    
    n = int(input())
    print("А Б В")
    for anya in range(1, n):
        for borya in range(1, n - anya):
            vova = n - anya - borya
            print(anya, borya, vova)


if __name__ == "__main__":
    main()
