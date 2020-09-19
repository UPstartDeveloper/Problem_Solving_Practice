def find_array_quadruplet(arr, s):
    '''Returns a quadtuple of elements in arr, that sum to s, in sorted order.'''
    solution = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                for k in range(len(arr)):
                    if k != j and k != i:
                        for l in range(len(arr)):
                            if l != i and l != k and l != j:
                                p1, p2, p3, p4 = (arr[i], arr[j], arr[k], arr[l])
                            if (p1 + p2 + p3 + p4) == s:
                                return sorted([p1, p2, p3, p4])
    return solution 




if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 7, 9]
    target = 20
    print(array_quadruple(nums, target))
