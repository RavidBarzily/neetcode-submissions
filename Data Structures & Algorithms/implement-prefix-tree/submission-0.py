class PrefixTree:

    def __init__(self):
        self.children = {}   # letter -> TrieNode
        self.is_end = False 

    def insert(self, word: str) -> None:
        current = self
        for ch in word:
            if ch not in current.children:
                current.children[ch] = PrefixTree()
            current = current.children[ch]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self
        for ch in word: 
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True