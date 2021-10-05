from heapq import heapify, heappush, heappop


def sort_k_messed_array(arr, k):
    if k > 0:
        index = k + 1  # window size
        # iterate a window over the array - put the elems in a heap
        window = arr[:index]
        heapify(window)  # k log k iterations
        while index < len(arr):  # n iterations
            arr[index - (k + 1)] = heappop(window)  # log k
            heappush(window, arr[index])  # log k
            # increment the index
            index += 1
        # add any last elements
        if len(window) > 0:
            for index in range(len(arr) - (k + 1), len(arr)):
                arr[index] = heappop(window)
    return arr


if __name__ == "__main__":
    # Test Cases
    arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    print(sort_k_messed_array(arr, k))

    arr = [6, 1, 4, 11, 2, 0, 3, 7, 10, 5, 8, 9]
    k = 6
    print(sort_k_messed_array(arr, k))


# Time: O(n log k)
# Space (k)
