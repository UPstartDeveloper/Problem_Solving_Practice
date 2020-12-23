# Connal 
# Zain


def word_count_engine(document):
    # A: clean it of any non alpha chars
    words = document.split()
    for index, word in enumerate(words):
        new_word = ""
        for char in word:
            if char.isalpha() is True:
                new_word += char.lower()
        words[index] = new_word
    # B: get a freq dist (dict), and an array of unique words
    unique_words = list()
    type_tokens = dict()
    for word in words:
        if word in type_tokens:
            # increment the key-value pair
            type_tokens[word] += 1
        else: 
            # init the key-value pair
            type_tokens[word] = 1
            # make an array of just the unique words, 
            unique_words.append(word)
    # C: bucket sort by the token count
    word_buckets = [list() for _ in range(len(words))]
    for word in unique_words:
        # let the index in word_buckets relate to the token count
        count = type_tokens[word]
        word_buckets[count - 1].append(word)
    #  # make a new 2D array for the return value
    sorted_words = list()
    # D: iterate the 1st in reverse
    for index in range(len(word_buckets) - 1, -1, -1):
        word_list = word_buckets[index]
        if len(word_list) > 0:
            # for each word type, 
            for word in word_list:
                # add a 2D array to the return list w/ the count
                word_count_as_strs = [word, str(type_tokens[word])]
                sorted_words.append(word_count_as_strs)
    # E: return the return value
    return sorted_words


"""# E: convert numbers to string
  for index, type_token_tuple in enumerate(type_tokens_list):
    type_of_word, token_count = type_token_tuple
    type_tokens_list[index] = [type_of_word, str(token_count)]
  # F: return the 2D array
  return type_tokens_list"""
"""
  w = words in document
  n = len go doc
  time O(n + w log w)
  space (O(w))
  
  
  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"
                    
      
   nw = "perfect"
   word = "perfect."
   words = [
      "Practice",   
      "makes",
      "perfect",
      "youll",
      "only",
      "get",
      "Perfect",
      "by",
      "practice",
      "just",
      "practice"
   ]  
   
   type_tokens 
    0 1 2 3 4 5 6 7 8 9 10
   [                      ]
   
   # make a 2D array the length of words
   # iterate over type_tokens
    # put the type in the array, at token - 1 index
   # make a new 2D array for the return value
   # iterate the 1st in reverse
    # for each type in the index,
      add a 2D array to the return
  # return the return value
    
   
   tt = {
    "practice": 3,
    "makes": 1,
    "perfect": 2,
    "youll": 1,
    "only": 1
    "get": 1,
    "by": 1,
    "just": 1
   }
   
   ttl = [
    ("practice", "3"),
    ("perfect", "2"),
    ("makes", "1"),
    ("youll", "1"),
    ("only", "1")
    "(get", "1")
    ("by": 1)
    ("just": 1),
   ]
               
               
               
               
               
               
               
               
  alphabetical chars
  greatest to least
  
  The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.
  
  input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"
                    
                    [Practice, makes, perfect, youll]
                    
                    ABCS it's easy as 123

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
          
          
          {
            practice: 3
            per
          }
          
  no numbers
  
  intuition:
  
  frequency dist
  type ---> # tokens
  
  sort ---> TimSort, stable
  
  approach:
  
  # A: clean it of any non alpha chars
  # B: split the str by " "
  #     --> get array of just words
  # C: get a freq dist (dict)
  # D: sort by the value in reverse (desc order)
  # E: convert numbers to string
  # F: return the 2D array
  [output] array.array.string
  
  """

