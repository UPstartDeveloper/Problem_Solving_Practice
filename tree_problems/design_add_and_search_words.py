from string import ascii_lowercase


class TrieNode:
    def __init__(self, char, is_terminal=False):
        self.char = char
        self.is_terminal = is_terminal
        self.children = dict((zip(
            ascii_lowercase,
            [None for _ in range(26)]
        )))
        

class Trie:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, word: str) -> None:
        # TODO: refactor
        
        def _recursive_helper(node, index):  
            # A: Base case: reached the end
            if index == len(word):
                node.is_terminal = True
            # B: Recusrive: not the end
            else:
                next_char = word[index]
                next_node = node.children[next_char]
                if isinstance(next_node, TrieNode) is False:
                    next_node = TrieNode(next_char)
                    node.children[next_char] = next_node
                _recursive_helper(next_node, index + 1)
        
        # start traversing down the trie
        first_char = word[0]
        if first_char in ascii_lowercase:
            first_node = self.root.children[first_char]
            if isinstance(first_node, TrieNode) is False:
                first_node = TrieNode(first_char)
                self.root.children[first_char] = first_node
            _recursive_helper(first_node, index=1)
    
    def contains(self, word: str) -> bool:
        # TODO: refactor
        
        def _recursive_helper(node: TrieNode, index):  
            # A: Base case: reached the end
            if index == len(word):
                return node.is_terminal
            # B: Recusrive: not the end
            else:
                next_char = word[index]
                next_node = node.children[next_char]
                if (
                    next_char in ascii_lowercase and 
                    isinstance(node.children[next_char], TrieNode)
                ):
                    _recursive_helper(next_node, index + 1)
                else:
                    return False
        
        # start traversing down the trie
        first_char, first_node = word[0], None
        if (
            first_char in ascii_lowercase and 
            isinstance(self.root.children[first_char], TrieNode)
        ):
            first_node = self.root.children[first_char]
            _recursive_helper(first_node, index=1)
        else:
            return False


class WordDictionary:
    """
    Leetcode: https://leetcode.com/problems/design-add-and-search-words-data-structure/
    
    # ASSUME . = 1 of any letter
    
    Input:  str, lower eng/.
    
    Output ---> functions
    
    Intuition:
        dict
        Trie <---- yes!!!!
        
    EC: 
        1) Invalid iput ---> "", invalid
        
    Approach:
    
        1) Trie:
            26-way tree
            root = ""
            
            
    """
    def __init__(self):
        # init the trie -- root node
        self.dictionary = Trie()
        # hashset of added words
        self.prev_added = set()
        

    def addWord(self, word: str) -> None:
        # check if already added
        if word not in self.prev_added:
            self.dictionary.insert(word)
            self.prev_added.add(word)
        

    def search(self, word: str) -> bool:
        if "." not in word:
            return word in self.prev_added
        else:
            return self.contains_with_set(word)
        
    def contains_with_set(self, pattern: str) -> bool:
        """fail fast algo to pattern match word w/ dict"""
        ### HELPER
        def _matches(word, pattern):
            if len(word) != len(pattern):
                return False
            for ndx in range(len(word)):
                if word[ndx] != pattern[ndx] and pattern[ndx] != ".":
                    return False
            else:
                return True
 
        ### MAIN
        for word in self.prev_added:
            if _matches(word, pattern):
                return True
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
