import re

from data_structures import trie as t


def rank(encoded_text: [], tt: t.Trie) -> dict:
    ranking = {}

    for encoded in encoded_text:
        only_alpha = re.split(r'[^a-zA-Z]', encoded)
        only_alpha = [s for s in only_alpha if s]
        i = 0
        for word in only_alpha:
            for j in range(len(word)):
                substrings = [word[j:], word[:-j], word[j:-j]]
                for substring in substrings:
                    if tt.search(substring.lower()):
                        i += 1

        ranking[encoded] = i

    return ranking
