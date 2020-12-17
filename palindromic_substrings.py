

# Palindromic Substring

# input: str

# output: palindromic substrings
# str

"""
can be duplicates
case-sensitive 

"abc" ---> "a", "b", "c"

"aaaa" --> "a", "a", "a", "a", "aa", "aa", "aa", "aa", "aaa", "aaa"," aaaa"
 ^^
 
"a big banana"

each letter's a substring (single spaces not included)

# intuition - 2 pters (multi char substrings)


how to tell if a string's a palindrome
- 2 pointers that come closer
aaaaaaa
 ^    ^
  

   ---> "aaaaaa
         s.   e
         bcaeacb
            s
            e

# init a list ---> store all the pals
# iterate over all the chars -- (s <-- e)
  # init 2nd pointer at the end
  # find out if that subtring's pal --> boundary cond vary based on even/odd
    # if yes - append to the list

# iterate over all the chars -( s --> e)
  # init 2nd pointer at the end
  # find out if that subtring's pal --> boundary cond vary based on even/odd
    # if yes - append to the list
# add all individual char to the list
# return the list

         012
input = "aaa"
         se
pals = ["aaa", "aa", "aa", "a", "a", "a"]
start = 2
end = 2


"""
class Memoize:
  def __init__(self, func):
    self.f = func
    self.cache = dict()

  def __call__(self, substring):
    if substring not in self.cache:
      self.cache[substring] = self.f(substring)
    return self.cache[substring]

@Memoize
def is_palindrome(substring):  # O(n)
    # linearly search for mismatched chars
    start = 0
    end = len(substring) - 1
    while start < end:
      if substring[start] != substring[end]:
        return False
      start += 1
      end -= 1
    return True


def get_palindromic_substrings(input):
  def get_all_substrings():  # O(n^2)
    substrings = list()
    # define the length of the substrings
    for length in range(1, len(input)):  # n iterationd
      start = 0
      end = start + length
      while end < len(input):  # n iteraio
        substrings.append(input[start:end + 1])
        start += length
        end += length
    return substrings

    # aaa - 6 substrings n!
    # n^2 --> get all substrings
    # O(n!n)
    # Space: O(n!)

  pals = [
    string for string in get_all_substrings() 
    if is_palindrome(string)
  ]
  pals.extend([
    char for char in input if char.isalpha()
  ])
  return pals

print(get_palindromic_substrings("aaa"))