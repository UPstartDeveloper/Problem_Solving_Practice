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


def drawing_book(book_length, target_page):
    '''Return the minimum number of page turns needed to reach a page.'''
    """
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

Test Cases

Variables   |  book_length | target_page | front_page_turns | back_page_turns |

Values      |       6      |      2      |        0         |      3          |

Oh no! it looks like this first approach incorrectly calculated both values for
the number of page turns. How can we refine the algorithm?

Idea #3 - "map" page numbers to an array index for the front page turns,
          and calculate the turns from the back using the total amount of
          "page pairs" in the book

          e.g. a book of 6 pages, and the target is page 5
          it can be represented like this:
             0        1       2      3
          [ (1,) , (2, 3), (4, 5),  (6,)  ]

          total pages that are paired together in the book: 4
          turns from the front: 2
          turns from the back: 1
          minimum number of turns is 1.
    """
    # calculate the length of an array that could repr pairs of page numbers
    if book_length % 2 == 0:
        num_page_pairs = (book_length / 2) + 1
    elif book_length % 2 > 0:
        num_page_pairs = (book_length // 2) + 1
    # exit early if possible
    if target_page == 1 or target_page == book_length:
        return 0
    # calculate the page turns needed, and return the minimum
    front_turns = int(target_page // 2)
    turns_from_back = int(num_page_pairs - (front_turns + 1))
    return min([front_turns, turns_from_back])


if __name__ == '__main__':
    print(drawing_book(6, 4))
