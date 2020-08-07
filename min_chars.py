import math 


def minimum_characters(phrase):
  # A: init num of minimumCharacters needed
  min_chars = 0
  # B: init the left and right indices = len(phrase) / 2
  midpoint = math.ceil(len(phrase) / 2) - 1
  right_index = left_index = midpoint
  # C: iterate from the center
  while left_index > -1 and right_index < len(phrase):
    # D: if not equal, 
    if phrase[left_index] != phrase[right_index]:
      print(f'{phrase[left_index]} not equal to {phrase[right_index]}')
      print(f'indices: {left_index}, {right_index}')
      # i: determine which side of the midpoint is a longer substring
      left_length, right_length = (
        len(phrase[:midpoint]),
        len(phrase[midpoint:right_index])
      )
      print(f'Lengths: {left_length}, {right_length}')
      # a: assume the left is longer
      left_is_longer = True
      # b: change if appropiate
      if right_length > left_length:
        left_is_longer = False
      # ii: return the length of substring of that side's index, till the end
      if left_is_longer is True:
        print(left_index)
        min_chars += len(phrase[left_index:]) - 1
        print('adding left:', len(phrase[left_index:]) - 1)
        print(min_chars)
      else:
        min_chars += len(phrase[right_index:]) - 1
        print('adding right:', len(phrase[right_index:]) - 1)
      # iii: exit out of the loop
      break
    else:  # if letters equal,
      # just move on to next iteration
      print("equal")
      left_index -= 1
      right_index += 1
  return min_chars
  
# Case 1: "DDFGFDDD" FAILING
# Case 2: "ABC" PASSED
# Case 3: "AACECAAAA" FAILING
phrase = "ABC"
print(minimum_characters(phrase))


"""
Variable - Value Trace
          0  1  2
phrase = "A  B  C"

min_chars = 2

midpoint = 1

right_index = 2

left_index = 0

left_length = 2

right_length = 2

left_is_longer = True


"""
    
  