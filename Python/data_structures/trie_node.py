class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False
