from collections import deque

class Vertex:
    def __init__(self, word):
        self.word = word
        self.neighbors = dict() # word --> Vertex(word)
    
    
class WordGraph:
    def __init__(self, src, target, words):
        self.src = src
        self.target = target
        self.words = words
        self.vertices = dict()
        self.transition = 0
        
    def get_1_edits(self):
        def is_1_edit_away(word, other_word):
            if len(word) != len(other_word):
                return False
            # iterate over both words
            num_differences = 0
            for index in range(len(word)):
                if word[index] != other_word[index]:
                    num_differences += 1
                if num_differences > 1:
                    return False
            return True
        # make a vertex for each word in words
        self.vertices[self.src] = Vertex(self.src)
        # add the starting word to the list of words
        self.words.append(self.src)
        # find which words are neighbors of each other
        for word in self.words:
            self.vertices[word] = Vertex(word)  # w= # words                         ^    
        for index in range(len(self.words)): # w iterations
            word = self.words[index]
            for other_index in range(len(self.words)):  # w iterations
                if index != other_index:
                    other_word = self.words[other_index]
                    if is_1_edit_away(word, other_word) is True: # w iteration
                        self.vertices[word].neighbors[other_word] = (
                            self.vertices[other_word]
                        )
        # check if that word is 1-edit
        # if so --> make it a
    
    def bfs(self, source, target):  # O(w + e)
        # init a queue
        q = deque()
        visited = set()
        transitions = 0
        q.append((self.vertices[source], transitions))
        paths = list()
        
        while q:
            # dequeue from q
            next_word, transitions_so_far = q.popleft()
            if next_word.word == target:
                paths.append(transitions_so_far)
            # visit()
            visited.add(next_word)
            neighbors = list(next_word.neighbors)
            for n in neighbors:
                neighbor_vertex = next_word.neighbors[n]
                if neighbor_vertex not in visited:
                q.append((neighbor_vertex, transitions_so_far + 1))
        if len(paths) > 0:
            return min(paths)
        return -1
 

def shortestWordEditPath(source, target, words):
  wg = WordGraph(source, target, words)
  wg.get_1_edits()
  return wg.bfs(source, target)
  # B: init a count ofr # of transitions
  # C: make the edits:
    # pick one randomly for the array of 1-edit words from the current
    # if we run of words to edit, then return -1
    # if we find a word --> make its list of 1-edit words 
      # increment # of transaitions
    # if edited == targets:
      # return transitions


"""
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

wg:
src = "bit"
target = "dog"
transitions = 0
vertices = {
  bit: V(),
  but: V(),
  put: V(),
  big: V(),
  pot: V(),
  pog: V(),
  dog: V(),
  lot: V(),
}




Functions
get_one_edit_word(word)


Approach
# A: geting all 1-edit word for the src word
# B: init a count ofr # of transitions
# C: make the edits:
  # pick one randomly for the array of 1-edit words from the current
  # if we run of words to edit, then return -1
  # if we find a word --> make its list of 1-edit words 
    # increment # of transaitions
  # if edited == targets:
    # return transitions
    
    
1-edit:

- be different by one letter, same length
- one word is longer/shorter by 1 letter                co    cot 
- 
"""