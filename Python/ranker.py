from data_structures import trie as t


def rank(encoded_text, tt: t.Trie) -> dict:
    only_alpha = []
    ranking = {}

    for encoded in encoded_text:
        cleaned = ''.join(c for c in encoded if c.isalpha() or c.isspace())
        only_alpha.append(cleaned)

        i = sum(tt.search(word.lower()) is not False for word in cleaned.split())
        ranking[encoded] = i

    return ranking
