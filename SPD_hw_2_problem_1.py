"""
Problem #1: Add Two Numbers
Leetcode URL: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

'''
1. Restate the problem:
Oh okay, so the the digits in each linked list need to be first reversed,
so that I know the value they really represent?
Then if I heard you correctly, the process is I have to add those two decimal
values (that just means a number in base ten), and then return that in a linked
list the same way as the numbers which we were given? Meaning that the number
(the digit value, not the whole value) is at the end the list, then preceded by
the digit that was to the RIGHT of it in the number, will be to the LEFT of it
in the linked list nodes?

2. Ask clarifying questions/State Assumptions
Ok this looks very interesting! Let me think for a second here... where would
we used this? This looks like it has some application in encoding and decoding
messages...

Can we assume this function needs to be able to handle linked lists of any
size, in terms of the number of nodes?
I'll assume so, since these are linked lists there's no restriction on the
size of the data we're receiving, save we run out of memory.

Are the two linked lists the same size as each other?
I'm assuming no, because we're decoding the values, and we should be able to
add any two decimal values regardless of their length.

And for right now, we're just concerned about summing 2 linked-lists right now?
I assume so - I know it says it right there in the problem, and that's what
I'll focus on for right now - but I'm totally down to improving it later to
handle more numbers (time permitting).

And what about the data type of the linked lists? I don't seem to recall a
built-in Python data structure for this, am I being provided with a Linked List
class here?
No? Okay, then I can just write up my own classes fairly simply.

It almost reminds me of the blockchain, you know? Linked lists and the
blockchain aren't exactly the same data structure - but maybe this function
could help us in same situation as Ethereum has, whenever they have to
verify a transaction. First we read in data from everyone's block, which in our
case is everyone's 2 or 3 sequence of linked list nodes, then we add up the
values stored in those pieces, then send off a new message encoded in a linked
list, before continuing with the rest of our process. I think it's really cool,
there's so many benefits to distributed systems in terms of scalability,
resistance to network failure, so on and so forth.

4a. Think out loud - Brainstorm solutions, explain rationale

Ok so in terms of our solution, when I look at the problem and I see the
example input you provided, there seems to be a really clear brute force
solution for this:

0. Write LinkedList and Node classes
1. "Decode" the first list - meaning we read in the number it represents
2. "Decode" the second list
3. Add the two values
4. "Encode" the sum value into a new linked list - convert it into what it
would look like in reverse, in terms of the nodes
5. return a new linked list

Everything here looks great so far - before coding it up we should probably
take a closer look at the decode() and encode() first, right?

'''
