def total(basket):
    '''# form a distibution of the copies of each book being bought
    book_orders = {}
    for book in basket:
        if book in book_orders:
            book_orders[book] += 1
        else:  # book not in book_orders
            books_orders[book] = 1
    # form the minimum number of sets from the population of books in basket
    pass
    # use the lengths of each set to calculate largest discount subtotal
    cost_one_book = 8
    order_discounts = {
        1: 0,
        2: .05,
        3: .10,
        4: .20,
        5: .25
    }'''
    # make the minimum number of sets from the basket
    book_orders = list()
    for j in range(len(basket)):
        book = basket[j]
        # adding book to an existing set
        for i in range(len(book_orders)):
            collection = book_orders[i]
            if book not in collection:
                collection.add(book)
                print(book_orders)
                break
        else:
            new_order = set([book])
            book_orders.append(new_order)
            # print(book_orders)
        # adding book as part of a new set
    # use the lengths of each set to calculate discount percentage
    # print(order_sets)
    cost_one_book = 8
    order_discounts = {
        0: 0,
        1: 0,
        2: .05,
        3: .10,
        4: .20,
        5: .25
    }
    # calculate subtotal
    total_cost = 0
    # print(total_cost)
    # total_cost = total_cost - (total_cost * order_discounts[num_orders])
    for i in range(len(book_orders)):
        order_length = len(book_orders[i])
        discount_rate = order_discounts[order_length]
        cost = (cost_one_book - (cost_one_book * discount_rate)) * order_length
        total_cost += cost

    return int(total_cost * 100)
