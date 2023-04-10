from data_structures import trie


def main():
    with open('utils/wordList.txt', 'r', encoding='utf8') as d:
        words = [line.strip for line in d]
        d.close()

    t = trie.Trie()

    for w in words:
        t.insert(w)


if __name__ == '__main__':
    main()
