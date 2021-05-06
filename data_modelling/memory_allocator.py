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


--------------------------------------
Memory Allocator:

Attr:
1) stores an array of memory. In our case:
    0 = free mem
    1 = allocated mem
2) atomic counter = increments for each time 
    an alloc(X) op is completed successfully (more on that later)
3) Maps an ID to certain ranges of allocated mem (based on atomic counter, 
                                        more on that later)
Methods:
1) alloc(num_blocks):
    - given int: num_blocks ==> 
        - go find the leftmost cont. block of free mem of len() == num_blocks
        - turn the memory to 1s
        - assign ID to the range
        - return the index where the range starts
    - if no range, return -1
2) erase(int: ID):
    - given ID 
    - find the range of memory assigned this ID
        - if found - 
            - turn the allocated memory free (1 -> 0), aka "delete"
            - return how many blocks were deleted (# array indices)
        - not found 
            - return -1

3) main(queries: List[List[int]])
- handle each query (array of 2 elements) in the following
    - if first element == 0: time for an alloc
    - if first == 1: time for an erase
    - second element = provides arg for num_blocks or ID, depending on case


"""


class MemoryAllocator:
    def __init__(self, memory_size):
        self.mem = [0 for _ in range(memory_size)]
        self.atomic_counter = 0
        self.register = dict()  # ID --> starting index, end_index

    def alloc(self, num_blocks: int) -> int:
        """
        TODO:
        1) how to find a cont. subarray of specified size?

        Intuition: search problem

        Approach:
        1) Brute Force:
            a) nested for loop
        2) 2 Pointers
            a) if range not found at first, move to find the next zero
            b) when found, bring the first pointer up to that spot

        Examples:
                     v
        [0,1,1,1,1,1,0,0,0], 2 --> 7
        [0,1,1,1,1,1,0,0,0], 1 --> 0
        """
        pass

    def erase(self, ID: int) -> int:
        # validate ID
        if ID not in self.register:
            return -1
        # ID found
        
        # erase operations
        erased = 0
        # return no. deleted blocks (i.e. deleted during execution)
        return erased if erased > 0 else -1
    
    def handle_queries(self, queries: list[list[int]]):
        '''Handles every valid query'''
        # init output
        results = list()
        for query in queries:
            # validate the query
            if len(query) == 2:
                # handle the query, store the result
                arg = query[1] 
                if query[0] == 0:
                    result = self.alloc(arg)
                elif query[0] == 1:
                    result = self.erase(arg)
                # add it to the list of results
                results.append(result)
        # return output
        return results
            
    
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
"""


Part II.

free blocks of memory

return the id
"""
