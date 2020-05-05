def total(basket):
    # make the minimum number of sets from the basket
    book_orders = list()
    for j in range(len(basket)):
        book = basket[j]
        # adding book to an existing set
        for i in range(len(book_orders)):
            collection = book_orders[i]
            if book not in collection:
                collection.add(book)
                # print(book_orders)
                break
        else:
            new_order = set([book])
            book_orders.append(new_order)
    # redistribution of books, so average number of books/order increases
    for i in range(len(book_orders)):
        if i < len(book_orders):
            order = book_orders[i]
            for j in range(len(book_orders)):
                if i != j:
                    if j < len(book_orders):
                        other_order = book_orders[j]
                        print(book_orders)
                        # if this order has no unique values versus another order
                        if (len(order - other_order) == 0 and not
                                len(order) >= len(other_order)):
                            print(f'Order: {order}')
                            print(f'Other order: {other_order}')
                            # transfer of book between orders
                            unique_books = other_order - order
                            book_to_give = unique_books.pop()
                            order.add(book_to_give)
                            other_order.remove(book_to_give)
                            # reassign into the book_orders array
                            print(i, j)
                            book_orders[i], book_orders[j] = order, other_order
                            '''del book_orders[i + 1]
                            if i < j:
                                del book_orders[j]
                            else:
                                del book_orders[j + 1]
                            print(book_orders)'''
    # use the lengths of each set to calculate discount percentage
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
    for i in range(len(book_orders)):
        order_length = len(book_orders[i])
        discount_rate = order_discounts[order_length]
        cost = (cost_one_book - (cost_one_book * discount_rate)) * order_length
        total_cost += cost

    return int(total_cost * 100)
