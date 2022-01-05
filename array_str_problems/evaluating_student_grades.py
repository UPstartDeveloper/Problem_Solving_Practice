class Solution:
    """You are given a string representing all letter grades a student as earned. 
       The record only contains the following three characters:     

        'A' : Excellent
        'B' : Good
        'C' : Average
        'D' : Below Average
        'F' : Deficient
    
       A student will be given a diploma if their record has:
       1) Less than 5 D's 
       2) Less than 2 F's
       3) No more than 3 consecutive D's
       
       Given a string, write a function to return whether a given student will be given a diploma.
    """

    def is_diploma_candidate(self, grades: str) -> bool:
        """Solution is O(n) time, O(1) space"""
        ### HELPER
        def _find_longest(grades):
            """find out the length of the longest sequence of consecutive D's"""
            index1, longest_length = 0, 0
            while index1 < len(grades) - 1:
                move_fwd = 0
                if grades[index1] != 'D':
                    move_fwd = 1
                else:  # grades[index1] == 'D'
                    local_length, first_ndx = 1, index1
                    while (
                        first_ndx < len(grades) - 1 and 
                        grades[first_ndx] == 'D' and
                        grades[first_ndx + 1] == 'D'
                    ):
                        local_length += 1
                        first_ndx += 1
                    longest_length = max(longest_length, local_length)
                    move_fwd = first_ndx + 1 - index1
                index1 += move_fwd
            return longest_length
                
        ### MAIN
        grades = grades.upper()
        num_ds_overall = ndo = grades.count('D')
        num_fs_overall = nfo = grades.count('F')
        longest_consecutive_ds = lcd = _find_longest(grades)
        return (
            ndo < 5 and nfo < 2 and lcd <= 3
        )


if __name__ == '__main__':
    # input, exp_output
    tests = [
        ('A', True),
        ('D', True),
        ('ABBDCDDD', True),
        ('ABDDCDDD', False),
        ('ADADADADADADADADADAD', False)
    ]

    sol = Solution()
    for grades_str, exp in tests:
        actual = sol.is_diploma_candidate(grades_str)
        assert actual == exp, f"Actual is {actual}, exp is {exp}"
