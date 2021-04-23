"""

array of ints, a
queries = List[List[int]]
q[i][0] = 0

query = [, number of indices to skip in a]
i = index

binary

a[i] = 0 = not allocated

Part I.

take the leftmost contiguous subarray
all 0s --> allocated them (turn them to 1)

if not, return -1 (no zeros)
if --> return starting index

Example:

i: [[0,0,0,0,0,1,1,1,0,1,0,1]]
output: 0


1. set an element to zero
2. finding the leftmost block of zeros

[1,1,1,1,1,1,1,1,1,1,1,0]

3. modify the array

4. return the index
         2
a = [0,1,0,0,0,1,1,0,0,0,1,0,0]
queries = [[0,2], [0,1], [0,1], [1,2], [1,4], [0,4]]
expected output = [2,0,4,1,-1,-1]


a, queries

for q in queries

    if q[0] == 0:
        alloc()
    else:
        erase()


"""


class Solution:

    def memory_allocator(self, a, queries):

        def alloc(query) -> int:
            # query[0]-, query[1] = number of zeros we have to fit in the contiguous
            num_bits = query[1]  # 2
            if num_bits == 1:
                return a.index(0)

            # return index of first 0 or -1
            starting_index = 0

            while starting_index < len(a):  # 2
                # look for the first zero 
                # if I find 0
                if a[starting_index] == 0:
                    index = starting_index + 1  # 3
                    num_zeros = 1  
                    # look for rest of required zeros
                    while index < len(a) and a[index] == 0:
                        num_zeros += 1  # 2, 3
                        index += 1  # 5
                        if num_zeros == num_bits:
                            return starting_index
                    num_zeros = 0
                    starting_index = index 
                else:
                    starting_index += 1               
            return -1

        def erase():
            return -1

        # A: init output arr
        output = list()
        # B: handle each query
        for q in queries:
            # if-else
            if q[0] == 0:
                output.append(alloc(q))
                found = output[-1]
                if found != -1:
                    for index in range(found, found + q[1]):
                        a[index] = 1
            else:  # erase query
                output.append(erase())

        # C: return the output
        return output


if __name__ == "__main__":
    
    a = [0,1,0,0,0,1,1,0,0,0,1,0,0]
    queries = [[0,2], [0,1], [0,1], [1,2], [1,4], [0,4]]
    expected_output = [2,0,4,1,-1,-1]

    sol = Solution()
    print(sol.memory_allocator(a, queries))






"""



Part II.

free blocks of memory

return the id
"""
