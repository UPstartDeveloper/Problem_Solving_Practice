"""
Problem
Given a string, str_a, return each word 
and the word frequency in descending order by frequency in the str.

Constraints

Not case sensitive. (New =! new)
A word does not contain any spaces
If a word ends with a punctuation mark, ignore it.
The order doesn't matter for words with the same frequency (therefore your answer may differ).

ASSUMPTIONS (added by me):
- the string contains only English alphabetical character 
(but we can remove this later)

Example Inputs:
1. 
 "Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la" -> [('la', 20), ('fa', 2)]
"lala"-> [('lala', 1)]
2. 
 "Fa la la la la, la la la la Fa la la la la, la la la la Oh no no Deck the halls with boughs of holly Fa la la la la, la la la la (fa la la la la, la la la la) 
 'Tis the season to be jolly Fa la la la la, la la la 
 la (fa la la la la, la la la la) Don we now our gay apparel Fa la la la la, la la la la (fa la la la la, la la la la) 
 Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la la la Fa la la la la, fa la 
 la la Fa la la la la, la la la la la la Fa la la la la, fa la la la See the blazing yule before us Fa la la la la, la 
 la la la (fa la la la la, la la la la) Strike the harp and join the chorus (Fa la la la la, la la la, fa la la la la, la la la) 
 Follow me in merry measure Fa la la la la, la la la la, fa la la la la, la la la la While I tell of Yuletide treasure 
 (Fa la la la la, la la la la) Fa la la la la, la la la la la la Fa la la la la, fa la la la Fa la la la la, la la la la la la 
 Fa la la la la, fa la la la Fast away, the old year passes Fa la la la la, la la la la (fa la la la la, la la la la) 
 Hail the new, ye lads and lasses (Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la) 
 Sing we joyous all together, oh Heedless of the wind and weather Fa la la la la, la la la la (hey) Fa la la la la, la la la la la la (oh) 
 Fa la la la la, fa la la la (oh) Oh oh fa la la la la, la la la la la la Fa la la la la, fa la la la Deck the halls with boughs of holly 
 Fa la la la la, la la la la 'Tis the season to be jolly Fa la la la la, la la la la Don we now our gay apparel Fa la la la la, la la la la 
 Troll the ancient Yuletide carol Fa la la la la, la la la la Fa la la la la, la la la la Fa la la la la, la la la la La la la la, la la la la" 
 -> [('la', 328), ('fa', 45), ('the', 12), ('oh', 6), ('of', 4), ('yuletide', 3), ('and', 3), ('we', 3), ('troll', 2), ('carol', 2), ('now', 2), ('holly', 2), ('jolly', 2), ('tis', 2), ('halls', 2), ('season', 2), ('boughs', 2), ('no', 2), ('apparel', 2), ('be', 2), ('our', 2), ('to', 2), ('deck', 2), ('with', 2), ('gay', 2), ('don', 2), ('ancient', 2), ('old', 1), ('follow', 1), ('joyous', 1), ('blazing', 1), ('in', 1), ('measure', 1), ('away', 1), ('chorus', 1), ('harp', 1), ('join', 1), ('weather', 1), ('new', 1), ('merry', 1), ('lasses', 1), ('while', 1), ('wind', 1), ('passes', 1), ('lads', 1), ('i', 1), ('together', 1), ('yule', 1), ('tell', 1), ('treasure', 1), ('year', 1), ('hey', 1), ('fast', 1), ('strike', 1), ('us', 1), ('hail', 1), ('me', 1), ('all', 1), ('heedless', 1), ('before', 1), ('see', 1), ('ye', 1), ('sing', 1)]


Intuition:
return an ordered frequency dist
|||||||||||||||||| = "fa"
||| - "la"

Approach:
- tokenize the string
- count the number of tokens for each type of word
- return in sorted order 

CQ:
- "ignore" - means to not include words that only appear once with punctuation
- what does puncutation mean to you --> "?, ., !"
- am I allowed to use built-in sorting functions? -- probably not

Edge Cases:
- if a type of word only appears once, but it ends with puncutation? - don't include it
- input is anything other than a single string --> guard clause

"The cat has a big hat."
--> [
    ("The", 1), ... ("hat", 0), OR hat is not in the output at all
]

Brainstorm:

1. Naive:
    # - tokenize the list
    # - make a dict for all of the type-num_token pairs
    #     - skip any that end in '!', '?', '.'
    # sort them as tuples in descending order
    # return the list
"""
from typing import List


def ordered_frequencies(corpus: str):
    def tokenize(corpus: str) -> List[str]:
        words = corpus.split()
        return words

    PUNCTUATIONS = [".", "?", "!"]
    # input validation
    if isinstance(corpus, str) is False:
        raise ValueError("corpus must be a string")

    # - tokenize the list
    tokens = tokenize(corpus)
    # - make a dict for all of the type-num_token pairs
    freq_dist = dict()
    for token in tokens:
        # check for punctuation
        if token[-1] not in PUNCTUATIONS:
            if token not in freq_dist:
                freq_dist[token] = 1
            else:
                freq_dist[token] += 1
    #     - skip any that end in '!', '?', '.'
    # sort them as tuples in descending order
    unordered_frequencies = list(freq_dist.items())
    # return the list
    return sorted(
        unordered_frequencies, reverse=True, key=lambda pair: pair[1]
    )


if __name__ == "__main__":
    pass
