"""
Problem #1: Add Two Numbers
Leetcode URL: https://leetcode.com/problems/add-two-numbers/

Description on LeetCode:
"
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.""

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

decode() => it takes in a LinkedList as input right? Oh no, even better if we
just made it a property of the LinkedList class!

the steps of this method
 we need to traverse the nodes
 we can take the value from each node, and add it to a sum variable
 (this can just keep incrementing, and that way even though it's out of order
 we'll end up with the true decimal value at the end)

 Oh, but we also have to make sure to be multiplying these by the power of ten,
 based on which power of ten we're at in the problem!
 Yeah - and that's fairly simple though, because the first value in the list
 is in the ones place, followed by tens

 so to speak, we can just keep another variable called exponent, and on each
 iterative step through the list we can make sure to raise 10 by that value,
 take that value and multiply it by the value in the Node, and THAT's what we
 can increment sum by!

Here's the pseudocode then:

LinkedList.decode():
    sum starts at 0
    exponent starts at 1

    data = grab next item from node, starting from the head

    sum += 10**exponent * data

    return the sum at the end


encode(sum):
    going from left to right, grab digits from the sum
    prepend them to the linkedlist (aka append them before the head node)
    return the linkedlist at the end

Did that make sense so far? ok then, let's jump into the code!

'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the next Node in the list


class LinkedList(object):
    def __init__(self, items=None):
        self.size = 0  # property for number of Nodes, starts at zero default
        self.head = self.tail = None
        # create the nodes of the list, if they are initially passed in
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        '''Returns a string representation of the list nodes in order.'''
        # init return string
        repr = ''
        # traverse over nodes to build the string
        node = self.head
        while node is not Node:
            data = node.data
            # make the string to repesent the next node data in overall repr
            if node == self.tail:
                repr += f" {data}"
            else:
                repr += f"{data} -> "
            node = node.next
        return repr

    def append(self, item):
        '''Adds a new item to the list.'''
        # construct a new Node
        node = Node(item)
        # add it to the linkedlist (as the head no previous)
        if self.size == 0:
            self.head = node
        # otherwise set it as the new tail
        # if there's no current tail
        elif self.size == 1:
            self.head.next = node
        # or if a tail already exists, set the node next to it
        else:
            self.tail.next = node
        # no matter what, set the new tail of the list to the new node
        self.tail = node
        # increment the size of the list
        self.size += 1

    def prepend(self, item):
        '''Adds an item at the front of a linked list.'''
        node = Node(item)  # make a new Node
        self.size += 1  # increment size of the list
        current_head = self.head  # save memory address of where head is now
        node.next = current_head  # ensure we don't lose the rest of the list
        self.head = node  # set the new node where it belongs

    def decode(self):
        """Return the decimal value corresponding to the sequence of ints in
           this list.

        """
        # init return value
        sum = 0
        # counter for the exponent value at each node in the list
        exponent = 1
        # start traversal from the head node, (may be None)
        node = self.head
        # traverse the list
        while node is not None:
            # increment sum
            sum += node.data * (10 ** exponent)
            # move the next node
            node = node.next
        return sum

    def delete(self, item):
        """Delete a node with the given item, or raise ValueError if not found.
           Implementation left blank for now, because not needed to solve this
           problem.

        """
        pass


def encode(value):
    """Return the linkedlist representation of a nonegative decimal integer.
       To implement this number, we need to slice off each integer, make a node
       for it, and insert it into the list somewhere.

       I see two ways of going about this:
       1. Left to right: We start by grabbing digits from the highest place
       value, then prepend each of them the linkedlist.

       2. Right to left: We grab digits from the lowest place value, then
       append them to the list.

       In terms of tradeoffs, neither approach has any clear benefit over the
       other. Both of these approaches scale in O(n) time, where n is the
       number of digits in the value.

       But since I'm left handed, I'll go with the first approach,
       because it seems more familiar to write from L to R for me:
       Google "cognitivie ease" if interested in learning more :)

    """
    # to figure out the place value of the front digit, I will begin by
    # modulo dividing the whole number by 10, and
    # count how many times I need to do this until the quotient is 0
    places = 0  # counter variable
    decimal = value  # copy of value, so we don't mdoify it
    while decimal > 0:
        places += 1
        decimal %= 10
    # next step: init a new linked list for the return value
    ll = LinkedList()
    # next step: adding nodes to the list
    while decimal > 0:
        # we take each integer off from the value
        next_digit = decimal // (10**places)
        # prepend to the list
        ll.prepend(Node(next_digit))
        # decrement places for the next iteration
        places -= 1
    # return the list at the end
    return ll


'''
To the interviewer:
If this looks like a lot, don't worry my friend - I agree with you!
I acknowledge if this concerns you, and will be sure to test this at the end,
so we can see if it actually works or not.
'''


def combine_linked_lists(list1, list2):
    '''Provide solution for the overall problem (see top).'''
    # decode the lists
    value1 = list1.decode()
    value2 = list2.decode()
    # find the sum
    sum = value1 + value2
    # return the encoded form of sum
    return encode(sum)


'''
To the interviewer:
Whew, that was a lot of work - and all for just 4 lines of code at the end!
Ok, now I test this with the input you provided, and of course I'm sure we
can find some ways to improve it...
'''

if __name__ == "__main__":
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # By the way, is it ok to input values like this using lists?
    # Sorry for not clarifying earlier!
    list1 = LinkedList([2, 4, 3])
    list2 = LinkedList([5, 6, 4])
    # Output: 7 -> 0 -> 8
    list3 = combine_linked_lists(list1, list2)
    print(list3)

'''
To the interviewer:
Discuss tradeoffs/Suggest improvements
Oh that's weird! I am not sure why it's not working - I'm sure it's just a
small runtime error somewhere, such as I didn't implement the __str__ magic
function correctly - and if I was doing this for real I'm sure I could look up
the fix in the Python docs reasonably fast.

Other than that, I like how our solution turned out!
In terms of Big O complexity for combine_linked_lists:

decode operations - O(n1 + n2), where n1 and n2 are the number of digits in the
                    first and second linked lists being decoded, respectively
computing sum - O(1), so we don't reall need to worry about that asymptotically
encode - O(m) - scales linearly to the number of digits in the sum

Hmm, I'm not sure how I could improve the runtime - but in terms of the actual
engineering, I think we could definitely improve this using another data
structure!

I think perhaps if we used a queue, it might help us in terms of pulling apart
the digits from the lists - instead of figuring out all the math, we could just
enqueue and dequeue. Again, the runtime complexity wouldn't change, it'd still
be in linear time since we have to go through all the digits, but in terms of
simplicity of code and the actual computations we have to process, we might be
able to shave off some time in the real world - and you know these blockchain
apps need to be high performance if they're going to compete!

That's all I got for now. What do you think?

'''
