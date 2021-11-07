"""
Purpose and Value of Each of the Problem Solving Steps:

1. Generate reasonable test inputs:
P - is to make sure you understand the kind of data you're working with
V - helps you to think in terms of concrete examples
    can see the edge cases

2. Solve the problem by hand
P - helps you build your algorithm
V - later on you can generalize, better communicate

3. Simplify the problem if needed
P - figure out the MVP of your solution
V - iterate on your solution, show interviewer you can work your way up

4. Find a pattern in your solution
P - generalize into code
V - now you're (almost) ready to code

5. Make a plan – Write pseudocode
P - figure out the high level strcuture of the code
V - mix and match ideas until you lego block build your way to the top

6. Follow your plan – Write real code
P - show the interviewer you can code
V - show what languages you know the libraries

7. Check your work – Test your code
P - make sure you didn't make any errors
V - shows the interviewer you're not careless


Good/Normal Input - one that is simple to solve
i.e. looking for a maximum in a list of ints, all the numbers

Bad/Unusual Input - one that you shouldn't have to deal with,
                    and should throw an error
i.e.

Edge Case Input - one that is rare
i.e.



1. Find the k largest values in an array of n numbers.
Return them in a new array sorted in decreasing order.
Good - [4, 6, 7, 8, 9], k = 2
Edge - k = n, where n = len(array)
Bad - k > n

array sorted? not
can there be duplicates? no
just postives integers

[4, 6, 8, 7, 9]
[9, 8, 7, 4, 6] -> [9, 8]


[4, 6, 7, 8, 9]
scores[-1] = 9
scores[-3]

scores[-(k - 1)]
Idea 1:
sort the array in decreasing order -
(O n * log n)
return the k numbers from the front of the array
return scores[0:k]


Idea 2:
[4, 6, 8, 7, 9], k = 2

[4 , 6]
[8, 6]
[8, 7]
[8, 9]


make subset for top k values
load the first k elements
iterate through one by one in the scores
    if the next element is greater than the current_min in our subset, replace
    with the new element

sort in decreasing order (insertion)

[8,| 9]

[9, 8]
"""


def find_min(scores):
    pass


def return_k_highest(scores, k):
    # scores.sort()
    # return scores[]
    top_score = scores[:k]
    current = 0

    scores = [4, 6, 8, 7, 9]
    k = 2
    print(return_k_highest(scores, k))


"""
2. Given an array a of numbers and a target value t,
find two numbers that sum to t (that is, a[i] + a[j] = t).
Good -> a = [10, 9, 7], t = 19
Bad -> strings in the array
Edge -> target cannot be made, or there's multiple ways to make the target

3. Given a list of n strings with mixed casing,
return a new list of all strings that start with a capitalized letter.
G - ['Spider', 'blocks', 'cat']
B - ['4']
E - ['Spider-Man']

4. Find the longest substring of unique letters in a given string of n letters.

"""


"""
Roman Numerals

everything below 3,099

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.
Symbol       Value
1V             5
10L            50C
100D           500M
1000
"""
