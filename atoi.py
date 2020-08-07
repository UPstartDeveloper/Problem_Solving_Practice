import math 


def atoi(a):
      # store a list of the characters we are looking for
      atoi_chars = [str(num) for num in range(10)]
      atoi_chars.append('-')
      # iterate until we find the first index with an acceptable char
      start = 0
      while start < len(a):
        char = a[start]
        if char == " ":
          start += 1
      # determine if this char is the start of a num
      if a[start] in atoi_chars:
          # iterate forward, find where the number stops
          end = start + 1
          while end < len(a):
              if a[end] in atoi_chars:
                  end += 1
              else:
                  break
          # slice the string and convert to an int
          number = int(a[start:end])
          # check the number is in range
          lower_bound, upper_bound = (
              -(math.pow(2, 31)), math.pow(2, 31) - 1
          )
          if number < lower_bound:
              return lower_bound
          elif number > upper_bound:
              return upper_bound
          else:
            return number
      else:   
        return 0

if __name__ == '__main__':
    a = "    -42"
    print(atoi(a))