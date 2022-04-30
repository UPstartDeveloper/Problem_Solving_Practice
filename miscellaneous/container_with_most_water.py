class Solution:
    # credit to golden-eagle
    # LeetCode: https://leetcode.com/problems/container-with-most-water/
    def maxArea(self, height: List[int]) -> int:
        # start w/ largest possible volume
        i = maxarea = h = 0
        j = len(height) - 1
        # find the max volume
        while i < j:
            h1 = height[i]
            h2 = height[j]
            b1 = j - i
            # move the smaller pter for next iter, to get best "next" vol
            if h1 > h2:
                area = h2 * b1  # compute the vol
                j -= 1
            else:
                area = h1 * b1  # compute the vol
                i += 1
            # update the biggest so far
            maxarea = max(maxarea, area)
        # all done!!
        return maxarea
