"""
Idea #1: Frequency Distributions

2 strings s and t are anagrams if they have the following characteristics:
- same types of letters, and nothing more than those types
- same # tokens for each of those types in both words

A: make a frequency distribution of the character types in s
   - using a dict
   - iterate over s
      - if we see a new character, add a new key value-pair
      - if we see a character seen before, increment its value
   - iterate over t, repeat the same process
B: compare the numbers of types of characters in each
C: make sure that each key in s appears in t, in the same amounts
   and vice versa
D: if all the checks pass, they are anagrams
"""
def make_histogram(string):
  # frequency distribution for string
  histogram = dict()
  for char in string:
    # add a new key
    if char not in histogram:
      histogram[char] = 1
    # increment existing key
    else:
      histogram[char] += 1
  return histogram

def valid_anagram(s,t):
  # frequency distributions
  s_histogram = make_histogram(s)
  t_histogram = make_histogram(t)
  # Check 1: number of character types
  s_types, t_types = (
    set(s_histogram.keys()), set(t_histogram.keys())
  )
  # take the intersection of the two, compare lengths
  common_types = s_types.intersection(t_types)
  if len(s_types) != len(common_types):
    return False
  # Check 2: frequencies of each type
  for key in s_types:
    if s_histogram[key] != t_histogram[key]:
      return False
  # All checks pass
  return True
      