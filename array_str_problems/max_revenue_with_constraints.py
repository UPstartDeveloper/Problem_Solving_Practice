from typing import List


class Solution:
    """
    You are given an nx3 array of jobs. 
    Each element in the array has the following attributes:
    
        Start Time: Time at which the job starts
        End Time: Time at which the job ends
        Revenue: Value associated with the job
    
    For example, if [1, 2, 50] is an element in an array of jobs, then:
        1 = start time; 2 = end time; 50 = revenue

    Given this information, write a function that 
    finds the maximum revenue for a set of jobs. 
    
    You must ensure that no two jobs selected have times that overlap 
    (e.g. the start time of one job does not occur before the end time of another).

    j1, j2 = 2 job arrs

    For example:
        input: jobs = [
            [1, 2, 50], 
            [1, 2, 100], 
            [7, 25, 100], 
            [6, 21, 45], 
            [3, 50, 200], 
            [7, 50, 400]
        ]
        
        output: "Optimal profit for this set of jobs is: 500"
        
        Explanation: two jobs that were selected here, [1, 2, 100] and [7, 50, 400]

    Input:
        0 <= start_time, end_time < pos_inf ---> dtype are ints
        revenue --> pos/neg, int/float
        max # of jobs: 1
        check that j1[1] < j2[0] ---> not is_overlapping
        jobs are not sorted by start_time

    Edge Cases:
        - no rows? ----> 0
        - jagged? invalid dtype -----> ValueError
        - TODO: test if all the jobs fall on the same timeline???

    Intuition:
             100          200
             50           400                         
        <---------------------------------------->  time
                    6----------21
            1 -- 2 3 ------------------------50
                        7-----------25
                        7--------------------50

             [100]            [400, 200, 45, 100]
            1 -- 2  3------------------------50

    Approach:

        1) Brute Force:

            A: "plot" all the jobs on the time
            B: merge all the overlapping jobs
            C: init max_revenue = mr = 0
                a) traverse all the overlapped jobs
                b) acculmulate mr by the highest revenue of the sub-jobs
            D: return mr

            ^HELPERS:

            jobs = [
                [1, 2, 50], 
                [1, 2, 100], 
                [7, 25, 100], 
                [6, 21, 45], 
                [3, 50, 200], 
                [7, 50, 400]
            ]
    
            _merge(jobs):

            {
                (start, end): [revenues for jobs in the time]
            }

            # init the dict 
            # traverse jobs
                # if job doesn't fit in key-value pair:
                    init a k-v pair
                # else:
                    update the revenue (i.e. the value) w/ largest so far
                    update the key with (min of starts, max times)
            # return dict        
    """
    def maximize_revenue(self, jobs: List[List[int]]) -> int:
        ### HELPERS
        def _group_jobs(jobs):
            # init the dict 
            job_groups = dict()
            # traverse jobs
            for start1, end1, revenue in jobs:
                pairs = list(job_groups.keys())
                for start2, end2 in pairs:
                    # if there's a fit - TODO[test]
                    if start2 <= end1 <= end2 or start1 <= end2 <= end1:
                        # update the revenue (i.e. the value) w/ largest so far
                        current_revenue = job_groups.pop((start2, end2))
                        largest_revenue = max(revenue, current_revenue)
                        # update the key with (min of starts, max times)
                        new_key = (min(start1, start2), max(end1, end2))
                        job_groups[new_key] = largest_revenue
                        break
                # if job doesn't fit in key-value pair
                else:
                    # init a key-value pair
                    job_groups[(start1, end1)] = revenue
            # return dict
            return job_groups 
        
        ### DRIVER
        # A&B: merge all the overlapping jobs
        job_groups = _group_jobs(jobs)
        #C: acculmulate max by the highest revenue of the sub-jobs
        max_revenue = sum(job_groups.values())
        # D: return output!!
        return print(f"Optimal profit for this set of jobs is: {max_revenue}")


if __name__ == "__main__":
    jobs = [
        [1, 2, 50], 
        [1, 2, 100], 
        [7, 25, 100], 
        [6, 21, 45], 
        [3, 50, 200], 
        [7, 50, 400]
    ]
    sol = Solution()
    sol.maximize_revenue(jobs)
