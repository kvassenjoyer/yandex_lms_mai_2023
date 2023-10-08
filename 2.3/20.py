def main():
    # Хайпанём немножечко!

    number_of_blocks = int(input())
    bad_block_index = -1

    previous_hash = 0
    for block_index in range(number_of_blocks):
        block = int(input())
        block_hash = block % 256
        random = (block // 256) % 256
        data = block // (256 * 256)
        hash_tester = (37 * (data + random + previous_hash)) % 256
        previous_hash = block_hash
        if block_hash > 99 or block_hash != hash_tester:
            bad_block_index = block_index
            break
    print(bad_block_index)


if __name__ == "__main__":
    main()
