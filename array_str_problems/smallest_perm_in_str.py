def get_shortest_unique_substring(arr, string):
    # both arr and str have 1 or more char
    # contiguous portion the str
    # arr = ['x','y','z'], str = "xyyzyzyx"
    #        'xyz'
    """
    "xyyzyzyyx"   xyz

    "ADOBECODEBANCDDD", ["A","B","C"] == > BANC  NABC

     'xyz'
     xyyz

    window equ to len of arr
    find a permuation of the arr in str

    # how to tell window = anagram(arr)
     # histogram is for 'xyy'
     {
       x: 1,
       y: 2
     }

     histogram for 'xyyz'
     {
     x: 1.
     y: 2
     z: 1
     }

     # assume that len(arr) <= len(str) ---> if not, return ""
     window size goes from len(arr) to len(str)
       start from looking for an substr len == len(arr):
         if found:
           return substr
         if !found:
           increment the size of the substr we
       return ""

    """

    def make_histogram(string):
        freq_dist = dict()
        for char in string:
            if char in freq_dist:
                freq_dist[char] += 1
            else:
                freq_dist[char] = 1
        return freq_dist

    def compare(substr_dist, arr_dist):  # O(a)
        for key in arr_dist.keys():  # a
            if key not in substr_dist:
                return False
        return True


def is_anagram(substr, arr_str):
    # "O(a + s)"
    substr_dist = make_histogram(substr)  # a
    arr_dist = make_histogram(arr_str)  # s

    return compare(substr_dist, arr_dist)  # a

    def make_arr_str(arr):
        return "".join(arr)

    if len(arr) <= len(string):
        # iterate from window sizes we have available
        #  input: ["A"], "A"
        #                             1         2
        for substr_length in range(len(arr), len(string) + 1):  # s - a iterations
            start = 0
            end = start + substr_length  # 1
            # have two indcies for the substr
            while end <= len(string):  # s iterations
                # compare to see if substr is an anagram
                substr = string[start:end]  # s
                found = is_anagram(substr, make_arr_str(arr))  # O(a + s)
                # if it is, return Early
                if found is True:
                    return substr
                start += 1
                end += 1

    return ""


"""


O((a + s) * s * (s - a))


O(a + s)


 arr = ['x','y','z'] 
 
 
 str = "xyyzyzyx"
 
 answer = ""
 substr_length = 3
 
start = 5
end = 8

substr = "zyx"
arr_str = "xyz"

found = True
 """
