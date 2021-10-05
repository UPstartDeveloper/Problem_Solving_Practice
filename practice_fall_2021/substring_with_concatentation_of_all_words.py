class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Assume:
        substring
        no empty 
        case insenstively
        
        Intution:
            1) permute all concatenations
            2) lookup concats in the s
            
        Approach:
            1) Brute force:
                 1) permute all concatenations - factorial time
                    ["bar","foo","the"]
                    b
                    f
                    t
                    _ _ _ 
                     
                    / \
              f__      b__
                     /\
                    bft btf
                 2) lookup concats in the s
                 for each permutation:
                    s.index(perm)
                 3)
            
        Edge Case:
            s = words together --> out: 0
            
        3 Keys:
        1) goal - full concatentation 
        2) choice -  words not used yet
        3) constraints - words list
        """

        def find_all_occurences(s, c):
            starts, s_index = list(), 0
            while s_index < len(s):
                # scan for first matching letter
                if s[s_index : s_index + len(c)] == c:
                    # scan through to make sure it is a whole substring match
                    starts.append(s_index)
                # always move to the next letter
                s_index += 1
            return starts

        def permute(choices: List[str], all_perms: set, current: List[str]):
            # Base Case:
            if len(choices) == 0:
                all_perms.add("".join(current))
                return
            # Recursive Case:
            else:
                for index in range(len(choices)):
                    choice = choices[index]
                    current.append(choice)
                    new_choices = [c for i, c in enumerate(choices) if i != index]
                    permute(new_choices, all_perms, current)
                    current.pop()

            return all_perms

        # A: form the permuatations of the concatenation
        concatenations = permute(words, set(), [])
        # B: look up each perm
        indices = list()
        for c in concatenations:
            indices.extend(find_all_occurences(s, c))
        # C: return the indices
        return indices

    """
    words = ["foo","bar"]       all_perms = {},     current = [bar]
                     ^
    new_choices = ["bar"]
     i = 0, 1
     -------------------------------------------------------
    #2 - POPPED
    c = ["bar"]                 ap = {}             curren = [foo, ]
    i = 0
  
    nc = []
    
     -------------------------------------------------------
     #3 - POPPED
      c = [""]                 ap = {             curren = [foo, bar]
                                foobar,
                              }
    """
