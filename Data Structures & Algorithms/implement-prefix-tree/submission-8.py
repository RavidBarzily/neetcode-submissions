class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
class PrefixTree:

    def __init__(self):
        self.prefixTree = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.prefixTree
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.end = True

    def walk(self, s):
        curr = self.prefixTree
        for ch in s:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr

    def search(self, word: str) -> bool:
        curr = self.walk(word)
        return curr.end if curr is not None else False
    

    def startsWith(self, prefix: str) -> bool:
        return self.walk(prefix) is not None
