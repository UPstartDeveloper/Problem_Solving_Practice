import math 


def minimum_characters(phrase):
    # A: init num of minimumCharacters needed
    min_chars = 0
    # B: init the left and right indices = len(phrase) / 2
    midpoint = math.ceil(len(phrase) / 2) - 1
    # C: iterate from the midpoint
    while midpoint > -1:
        # set indices for left and right
        left = right = midpoint
        print(midpoint)
        #  while phrase[left] == phrase[right]:
        while left > -1 and right < len(phrase):
            # D: check letters from left and right
            if phrase[left] == phrase[right]:
                print(f'Letters {phrase[left]} at {left} = {phrase[right]} at {right}')
                # move left and right
                left -= 1
                right += 1
                print(left, right)
            else: # letters don't match
                # move midpoint left and start over
                midpoint -= 1
                break
        # if there are index errors
        if left == -1 or right == len(phrase): 
            # find the longer side
            left_length = len(phrase[:left])  
            right_length = len(phrase[right:]) 
            # add on the length of remaining characters on this side
            if left_length >= right_length:
                min_chars += left_length
            else:
                min_chars += right_length
            # break out of the outer loop
            break
    return min_chars



"""
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

"""
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
    
if __name__ == '__main__':
    # Case 1: "DDFGFDDD" FAILING
    # Case 2: "ABC" PASSED
    # Case 3: "AACECAAAA" FAILING
    phrase = "AACECAAAA"
    print(minimum_characters(phrase))