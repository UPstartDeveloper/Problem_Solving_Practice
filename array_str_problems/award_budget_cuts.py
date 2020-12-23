def find_grants_cap(grantsArray, newBudget):
    """
    hey how u doin 

    let me try to join again

    ok

    N = num of grants
    newBudget = $$ of budget

    grants > cap ===> grant = cap
    grants <= cap ===> no change

    find cap 
    optimize for the minimal impacted_grants

    return cap

    floating pt
    nonnegative
    duplicates are ok

    grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

    A: take the sum of the whole input
    [2, 100, 50, 120, 1000]  -->  1272
    [2, 38, 38, 38, 38] --> <= 190
    78 + 38 = 116 + 38 = 154
    return 3

    b: Difference
        1272
        -190
        
        
    C: 
    upper bound for cap
    newBudget / N =  190 / 5 = 38
    lower bound = min(grantsArray)

    [2, 50, 100, 120, 0]
    82
    1082

    1000 - x = 38
    diff: 1082 - x = 82

    return max(grantsArray)

    - sorting

    -# [2, 47, 47, 47, 47]

    # A: set the initial bounds for the cap:
    - set the number of grants = len(gA)
    - lower: nB / len(gA)
    - higher: nB
    # B: init a sumSoFar = 0
    - see which values in the array are < lower:
        - add those to the sSF
        - decrement num of grants
    - if none are lower --> return the lower
    # C: at the end of high pass, recalculate the lower bound

    """
    # A: take sum of grantsArray (currently)
    current_sum = sum(grantsArray)
    # B: find the surplus (sum - newBudget)
    surplus = current_sum - newBudget
    # C: sort the grantsArray in reverse
    grantsArray.sort(reverse=True)
    # D: modify the grant amouts until surplus --> 0
    index = 0
    while surplus > 0:
        # get the grant amt at the current index
        amt = grantsArray[index]
        # if amt < surplus, set it to 0
        if amt <= surplus:
            grantsArray[index] = 0
            surplus -= amt
        else:  # amt > surplus
            grantsArray[index] = amt - surplus
            surplus = 0
        # reduce the surplus by that amt
        # move ahead in the array
        index += 1
    # E: return max(grantsArray)
    return max(grantsArray)