"""
Problem found on Hacker Rank:
https://www.hackerrank.com/challenges/drawing-book/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


Observations About the Problem:
- the last page, and n
  if n is odd, then that means the last page number is odd. Likewise, it is
  also printed on the front of a page;
  however if n is even, then the last page number is even, and it is printed
  on the back side of a page
- counting forwards, we start from 1
    e.g. if you want to get to page 2, the min number of page turns you need
        is 1, because it's only one page away from page 1

Idea #1 - subtraction
A: calculate the difference between p and 1
B: calculate the difference between n and p
C: return the lesser of the two

Idea #2 - looking at page turns
A: figure out which will result in fewer page turns:
    - turning from the front will always require p - 2 turns
        - edge case: (unless p == 1, where you need 0 page turns)
    - how many page turns do you need from the back?
        - if n is even, then you can only have 0 page turns if p == n
        - if n is odd, then the page turns you need from the back is
            n - (p + 1)
B: compare the two numbers for the page turning:
    - if equal, then just return the number
    - if unequal, then return the lesser of the two

"""


def drawing_book(target_page, book_length):
    '''Return the minimum number of page turns needed to reach a page.'''
    # calculate number of page turns from the front
    if target_page > 1:
        front_page_turns = 0
    else:
        front_page_turns = target_page - 2
    # calculate number of page turns from the back
    if book_length % 2 == 0 and target_page == book_length:
        back_page_turns = 0
    else:
        back_page_turns = book_length - (target_page + 1)
    # return whichever number results in less turns
    if front_page_turns != back_page_turns:
        return min([front_page_turns, back_page_turns])
    return front_page_turns
