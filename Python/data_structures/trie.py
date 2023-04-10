from trie_node import TrieNode


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


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in data_structures",
              "Present in data_structures"]

    # Trie object
    t = Trie()

    # Construct data_structures
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
