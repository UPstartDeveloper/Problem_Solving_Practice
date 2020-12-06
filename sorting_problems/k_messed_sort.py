from heapq import heapify, heappush, heappop


def sort_k_messed_array(arr, k):
    if k > 0:
        index = 0
        # iterate a window over the array - put the elems in a heap
        window = arr[:index + k + 1]
        heapify(window)  # k log k iterations
        END = len(arr) - k
        while index < len(arr):  # n iterations
            # compare the heap root to the idx
            elem = arr[index]
            # heappush(window, elem)
            root = heappop(window)
            if elem > root:
                # find where root is located
                for root_index in range(index + 1, index + 1 + k):
                    if arr[root_index] == root:
                        # swap
                        arr[index], arr[root_index] = (
                            arr[root_index], arr[index]
                        )
                        break
            # increment the index
            index += 1
            # add to the heap if needed
            if index < END:  # k iterations
                heappush(window, arr[index + k])
    return arr


if __name__ == "__main__":
    # Test Cases
    arr = [1,4,5,2,3,7,8,6,10,9]
    k = 2
    print(sort_k_messed_array(arr, k))

    arr = [6,1,4,11,2,0,3,7,10,5,8,9]
    k = 6
    print(sort_k_messed_array(arr, k))


# Time: (k * log k) + (k * 1) + (n * k)