from max_heap import BinaryMaxHeap


class Solution:
    def max_of_sliding_subarray(self, nums, k):
        index = k
        sub_maxes = list()

        heap = BinaryMaxHeap(nums[:k])

        for _ in range(len(nums) - k + 1):
            sub_maxes.append(heap.delete_max())
            # check if any inserts left
            if index < len(nums):
                heap.insert(nums[index])
                index += 1

        return sub_maxes


if __name__ == "__main__":
    array, k = [9, 4, 5, 3, 7, 8], 3
    sol = Solution()
    print(sol.max_of_sliding_subarray(array, k))  # [9, 5, 7, 8]
