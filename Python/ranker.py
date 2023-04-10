from data_structures import trie as t


def rank(encoded_text, tt: t.Trie) -> dict:
    only_alpha = []
    ranking = {}

    for encoded in encoded_text:
        i = 0
        for word in encoded.split():
            for j in range(len(word)):
                substring = word[j:]
                while tt.search(substring):
                    i += 1
                    substring = substring[:-1]

    # for encoded in encoded_text:
    #     i = 0
    #     for word in encoded.split():
    #         hold = word
    #         for _ in range(len(word)):
    #             secondary = hold
    #             while tt.search(secondary):
    #                 i += 1
    #                 secondary = secondary[:-1]
    #             hold = hold[1:]

        ranking[encoded] = i

    return ranking
