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
    """
    def get_sum(grantsArray, cap):
        sum_with_cap = 0
        for grant in grantsArray:
            if grant <= cap:
                sum_with_cap += grant
            else:  # grant > cap
                sum_with_cap += cap
        return sum_with_cap
    # sort the grants in reversem see if any can help us meet the budget
    grantsArray.sort(reverse=True)
    for cap in grantsArray:
        # get the sum we get from having this cap
        sum_with_cap = get_sum(grantsArray, cap)
        # print(sum_with_cap)
        # if sum is <= newBudget:
        if sum_with_cap <= newBudget:
            # return the cap + spare change
            return cap + (newBudget - sum_with_cap)
    # if none of the grant values work, return the average
    return float(newBudget) / len(grantsArray)
    """
    """
    # A: set the initial bounds for the cap
    num_grants = len(grantsArray)
    lower = float(newBudget) / len(grantsArray)
    higher = newBudget
    # B: meet the newBudget value
    # init the number of people who meet the cap's lower bound
    # meeting_cap = 0
    sum_so_far = 0
    # while meeting_cap < len(grantsArray):
    while num_grants > 0:
        # see which values are < lower bound:
        remaining_budget = newBudget
        for index, grant in enumerate(grantsArray):
            if grant <= lower:
                # add the amoumt, because we know we'll keep it
                sum_so_far += grant
                remaining_budget -= grant
                # meeting_cap += 1
                # decrement the number of grants we need to change
                num_grants -= 1
            else:  # grant > lower
                # grantsArray[index] = lower
                sum_so_far += lower
        # see if we've found the optimal cap
        if sum_so_far == newBudget:
            return lower
        elif num_grants == 1:
            return float(newBudget - sum_so_far)
        # C: otherwise at the end of high pass, recalculate the lower bound
        # print(sum_so_far, num_grants, lower)
        # lower = float(newBudget - sum_so_far) / num_grants
        lower = float(remaining_budget) / num_grants
        # "reset" for the next pass
        # meeting_cap = 0
        sum_so_far = 0
        num_grants = len(grantsArray)
    """
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
"""
    # sort the grants in reversem see if any can help us meet the budget
    grantsArray.sort(reverse=True)
    # add 0 as the lowest possible value the cap can be
    grantsArray.append(0)
    # early exit - if the surplus is there, the cap is the largest value
    surplus = sum(grantsArray) - newBudget
    if surplus <= 0:
        return grantsArray[0]
    # find the min number of grants to impact
    index = 0
    while index < len(grantsArray) - 1:
        grant = grantsArray[index]
        surplus -= (index+1) * (grant - grantsArray[index + 1])
        print(f"Surplus is now: {surplus}, grant is {grant}")
        if (surplus <= 0):
            break
        index += 1
    grants_affected = index + 1
    # calculate the cap (the grant needed to balance out the surplus, or
    # if we went beneath the newBudget this adjusts to make sure we're in
    # the right spot between grant values to be at no surplus)
    return (-surplus / float(grants_affected)) + grantsArray[grants_affected]


if __name__ == "__main__":
    grantsArray, newBudget = [2,100,50,120,167], 400
    print(find_grants_cap(grantsArray, newBudget))

    grantsArray, newBudget = [2,100,50,120,1000], 190
    print(find_grants_cap(grantsArray, newBudget))
