"""
Ctci, Chapter 6 - "Additional Questions" on Big O

Answers:

1. O(b) - b iterations of the for loop

2. O(b) - b stack frames

3. O(1) - mathematical ops

4. O(a / b) - the number of iterations of the while loop

5. O(log (n)) - each stack frame cuts down the possibilites by 2

6. O(n ** 1/2) - num of iterations to find the square root

7. O(n), where n = # of nodes in the tree.
   E.g. consider looking up the largest value in a BST that
   looks like a linked list going to the right

8. O(n), where n = # of nodes in the tree
   This is because we cannot rely on binary search, and instead
   fall back on using DFS/BFS.

9. O(n ** 2), where n = len(array) passed to copyArray().
   This is because the number of calls this function takes models 
   the Triangular Series (n * (n - 1) / 2) ---> then we drop the constants 
   and non-dominant terms.


   Examples
   n = 5
                                Number of iterations in appendToNew
    Outer loop iteration: 1     I
                          2     II
                          3     III
                          4     IIII
                          5     IIIII

10. O(log(n)) - base10 log, not base2, b/c number of iterations of loop.

11. O((numChars ** k) * k)
    The first term here models the time it takes to generate all the stack frames
    in the "call tree" - it follows the formula O(branches ** depth).
    Then, the last part we need to account for is after each of the strings is made,
    we check if it's sorted - this is k iterations.

12. O(b * log(b) + a * log(b)) = O((a + b)(log(b))
    First need to account for the sorting operation
    And then, for the repeated binary searches

"""
