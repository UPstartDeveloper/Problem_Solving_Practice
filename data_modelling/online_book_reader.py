"""
CtCI: 

7.5 Online Book Reader: 
Design the data structures for an online book reader system.

- Who?
    - mobile user - leisure, enterain
    - library card - want to access catalog from device
    - individual people 
    - central db for all books 

- What? 
    - library
    - browse books, check in/out books, read books

- How?
    - browse books, check out books, read books --> check in the book

- Where? - from home

1) core objects:
    A: Member:
        - {TODO} Librarians: giving recommendations, 
        - Reader: viewing the text
    B: Book
        - Genre
        - Author
        - Title
        - Year
        - Text -> [TODO]
        - # available copies

2) relationships: 1:1, 1:Many, Many:Many
    A: each user has their own copy of the book, only have 1 book at a time
    B: each user has many books, each book copy has 1 user at a time (realistic) <--
    C: each user has many books, each book can be checked out to users at a time

3) Actions:
    1) Reader.search(...) <-- some Book property
    2) Book.is_available() <-- can the book be checked out?
    3) Reader.checkout(book) <-- decrement # of available copies, 
                                    prevent readers from having +1 copies of a given book
    4) Reader.view(book) <-- TODO: UI component
    5) Reader.return(book) <-- increment # of available copies

4) DS:
    1) HashTable: BookCatalog.collection
        - Book_title --> book obj 
        - support fast lookup, check availability
    2) HashTable: Reader.checkedOutBooks
 
"""
