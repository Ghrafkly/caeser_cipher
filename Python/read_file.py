from data_structures import trie as t


def read_file() -> []:
    words = []
    with open('utils/wordList.txt', 'r', encoding='utf8') as d:
        for line in d:
            words.append(line.strip().lower())
    return words


def load_dictionary(words) -> t.Trie:
    data = t.Trie()
    for w in words:
        data.insert(w)
    return data
