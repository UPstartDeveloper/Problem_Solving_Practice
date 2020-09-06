def array_quadruple(nums, target_sum):
    for i in range(len(nums)):
        i_num = nums[i]
        for j in range(len(nums)):
            if j != i:
                j_num = nums[j]
            for k in range(len(nums)):
                for l in range(len(nums)):


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 7, 9]
    target = 20
    print(array_quadruple(nums, target))