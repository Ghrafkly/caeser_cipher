class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = {}

    # noinspection PyMethodMayBeStatic
    def get_node(self):
        return TrieNode()

    # noinspection PyMethodMayBeStatic
    def char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word) -> None:
        start = self.root
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True

    def search(self, word):
        start = self.root
        for i in word:
            if i not in start:
                return False
            start = start[i]
        return '$' in start
