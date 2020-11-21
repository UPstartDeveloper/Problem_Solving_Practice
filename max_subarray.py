class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Problem info: 
        - don't need to return the subarray, just the sum of its values
            - follow-up: could there be more than one array that leads to 
            the largest sum?
                - assume if we are asked to return the subarray, go with 
                the one that's smaller/first
        - if there's only one number, the sum is that number
            - is it guaranteed the list will have just one number? 
                - yes
                - and if there happens to be no elements, just return 0
                
        - positive and negative
        - can have duplicates
        - list is unsorted
        
        - can have up to 20,000 elements
        - have 32-bit integers 
        
        Insights:
        - initialize the sum at zero
        - if no negatives in the list -> return the sum of the whole thing  
        - O(n)
        - if list is one element -> add that element to zero, and return - 
        O(1)
        - if the list has negatives and has more than 1 element: -
            - here, we know that there's a possibility that the sum we need 
            to return,
                includes less than all of the array elements 
        
        Answer has both a Lower Bound, and a Higher Bound
        
        Lower Bound (if it has negatives or not)
            - maximum element
            
        Higher Bound - ideally the answer we need to return
        if no negatives:
            return the sum of the whole list 
                - because every int is >0, when we add more to the sum, the 
                sum gets bigger
        else (>=1 elements, and negatives):
            this is where the problem gets more tricky
            we know that higher bound >= lower bound
                [-4, -4, -4, -1]
                when we have negatives (either all or some)
                - then we know the sum to return, might just be the maximum
                - now we just want the max, because the less negatives 
                added to the sum, the higher it will be
                
        Okay, so the algo is almost complete!
        
        We just have to find a way to solve for when there negatives 
        present in the list, then go ahead
        and write psedudocode, real code, and test by hand on the given 
        inputs!
        
        Idea #1: Move from the outside of the array, in towards the largest 
        
        A: set lower bound =  max element
            - also, keep track of the index of the max
        
        B: early exit
        if just one element:
            return the lower bound
            
        C: find the higher bound
        
            - set two pointers at the left and right ends of the list
            - find the sum of the elements in between the pointers, 
            inclusive
            (at this point, whether the sum is >, < the max is unimportant, 
            we still need to figure out if 
            it's the highest possible sum)
            while the current_sum < lower_bound:
                i: get the elements at left and right indices
                ii: if either is negative,
                    - move that index inwards,
                    - and update the current sum so it increases
            [4, -7, -5, 6, 7, -7, 6]
            
            right answer: 13
            output: 
            
        
        Idea #2: Move from the inside of the array, outwards
        
        A: start by finding the max elem, and its index
        C: init two pointers, at the max_element index
        D: init current sum to lower bound
        E: init a list of sums, starting with lower_bound (so we can 
        remember the candidates for the largest   
            sum)
            
        F: while the left and right pointers don't cause IndexErrors: (stop 
        conditions at array ends)
            - move them one space to left/right
            - get the values at those indices
            - add to the current sum
            - if current sum is greater than lower bound, 
                then append to the list of candidates
        if one sides longer than the other, then after breaking from this 
        loop, 
            do the same for whatever side whose pointer didn't reach the 
            end
        G: return the max from the candidates list
        
                 0 1  2.3  4.5 6  7 8
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        
        lower_bound = 4
        max_elem_index = 3
        candidates = [4, ]
        
        left_index      |     right_index       |      current_sum
            1        |           4             |           4
        
        
        
        
        
        
                0  1  2.3  4.5 6  7 8
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        -2 + 1 = -1 
        
        lower_bound = 4
        max_elem_index = 3
        
        left_index      |     right_index       |      current_sum
            1          |           8           |           3
        
        (I'm going to go with the first index where the max appears
        tbh I'm not sure if it'll make a huge difference yet, we'll see as 
        we pesudocode,
        although one clear benefit of using the first is it's simpler, and 
        we use the in-built methods to do 
        it that way)
        
        
        """
        # count the number of negatives
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += 1
        # early exit: no negatives, so return the whole array
        if negatives == 0:
            return sum(nums)
        # early exit: if 1 or 0 positives, return the least negative
        if negatives >= len(nums) - 1:
            return max(nums)
        # otherwise: store the max subarray, for each possible size
        size_max_arr = dict()
        size_max_arr[len(nums)] = (sum(nums), nums)
        size_max_arr[1] = (max(nums), [max(nums)])
        # find the maximum subarray for each size in between:
        for subarray_size in range(2, len(nums)):
            # store all possible subarrays of this size in a dict
            sum_subarr = dict()
            # init pointers for the start and ending indices of each subarr
            start, end = 0, subarray_size
            while end <= len(nums):
                # get the subarray found between these indices
                subarray = nums[start:end]
                # get the sum of this subarray
                sum_value = sum(subarray)
                # store in the dict
                if sum_value not in sum_subarr:
                    sum_subarr[sum_value] = subarray
                # then increment the indices
                start += 1
                end += 1
            # find the maximum subarray of this size
            largest_sum = max(list(sum_subarr.keys()))
            # add it to the dict of all the sizes
            largest_arr_this_size = sum_subarr[largest_sum]
            size_max_arr[subarray_size] = (
                (largest_sum, largest_arr_this_size)
            )
        # find the subarray with the largest sum, among all sizes
        sorted_sums_and_subarrays = (
            sorted(list(size_max_arr.values()), reverse=True, key=lambda x: x[0])
        )
        largest_sum, largest_subarray = sorted_sums_and_subarrays[0]
        # return that subarray
        """
        largest_sum = nums[0]
        # set the size of the subarray
        sub_size = 0
        while sub_size < len(nums):
            # find all subarrays of that size in the whole array
            start_index = 0
            end_index = start_index + sub_size
            while end_index < len(nums):
                sub = nums[start_index:end_index + 1]
                # calculate their sum
                sub_sum = sum(sub)
                # compare it to the largest sum we've seen so far
                if sub_sum > largest_sum:
                    largest_sum = sub_sum
                # increment the indices
                start_index += 1
                end_index += 1
            sub_size += 1
        # return the largest sum
        return largest_sum
        """
        return largest_sum
        
"""
negatives = 2

size_max_arr ={
    2: 
}

sum_subarr = {
    
}

subarray_size
3

[-2,1,-3,4]


"""
        