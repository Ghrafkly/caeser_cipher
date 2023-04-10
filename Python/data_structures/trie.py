class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        crawl = self.root
        length = len(key)

        for level in range(length):
            index = self.char_to_index(key[level])

            if not crawl.children[index]:
                crawl.children[index] = self.get_node()
            crawl = crawl.children[index]

        crawl.is_end_of_word = True

    def search(self, key):
        crawl = self.root
        length = len(key)

        for level in range(length):
            index = self.char_to_index(key[level])

            if not crawl.children[index]:
                return False
            crawl = crawl.children[index]

        return crawl.is_end_of_word

# The below functions achieve the same as the trie object by using
# nested dictionaries
# def insert(words) -> {}:
#     data = {}
#
#     for word in words:
#         node = data
#         for char in word:
#             node = node.setdefault(char, {})
#         node['_end'] = '_end'
#     return data
#
#
# def search(word, data):
#     node = data
#     for char in word:
#         if char not in node:
#             return False
#         node = node[char]
#     return '_end' in node
