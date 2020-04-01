'''
Given an array a, write a function that executes n left rotations on the array.
E.g. [1,2,3,4,5] => [2,3,4,5,1]
Restate the question
Ask clarifying questions
State your assumptions
Brainstorm solutions
'''


'''
So if I understand the problem,
a left rotation is basically taking whichever list element is at the front,
moving it to the end,
and then all the elements shift over to the left,
for as many as n repetitions

ok, so I have a few questions:

1. is the list an array or a linked list?
2. is the list sorted?
3. is the size of the array allowed to change?
4. what is the return value?

I'm assuming that it's an array, and that the array is unsorted, and that
for the output I have to output what the final array looks like
(can it be the same variable as was given?)

So let me come up with a test case for this problems, because there's
definitely a few ways we could do it.

i.e.
a = [1,2,3,4,5]
n = 5

my brute force would be to name a new list called b, that starts out as the
same list as a

b = a

then I guess I could use a for loop, because we're doing this (left rotation)
for a certain number of repetitions (for i in range(n))

...
for data structures, I could use a queue!

'''
'''
Write a function that takes two lists named a and b, and returns a list
of common values that are in both lists.

# return a new list
# intersection between two lists
# are we returning a new array or linked?
# is it sorted? no
# duplicates? yeah, but not in output

a = [1, 2, 4, 5, 6, 5]
b = [2, 2, 5]

output = [2, 5]

# 1. find out which of these lists has less unique
# step 1, find the smaller list, search for unique values in the other list
# return the duplicates

b_len = len(b)
a_len = len(a)

if a_len < b_len:
else:
'''
