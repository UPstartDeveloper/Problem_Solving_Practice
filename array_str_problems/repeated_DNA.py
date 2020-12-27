class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        input: is a string 
        - length between 0 and 100,000
        - all upper case
        - either 'A', 'C', 'G', 'T'
        
        repeated = occurs more than once
        
        output:
        list of repeated substrings
                    AAAAACCCCCAAAAACCCCC  
        Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        Output: ["AAAAACCCCC","CCCCCAAAAA"]
        
        questions:
        can the start of the substrings overlap? yes
        
        Idea 1: Histogram
        
        # Intuition: use a sliding window to find all the substring types (10 chars)
                     store the number of occurences of each
                     return all that appear +1 times in an array
        Approach:
        
        # A: init the histogram (use a dict)
        
        {
        "AAAAACCCCC": 2,
        }
        # B: find all occurences of 10-letter DNA
            # enumerate their occurences
        # C: iterate over the key-value pairs, pick out the ones w/ 1+ occurences
        """
        # A: init the histogram (use a dict)
        histogram = dict()
        # B: find all occurences of 10-letter DNA
        start, end = 0, 10
        while end <= len(s):
            substring = s[start:end]
            # enumerate their occurences
            if substring in histogram:
                histogram[substring] += 1
            else:  # first time we've seen the substring
                histogram[substring] = 1
            start += 1
            end += 1
        # C: iterate over the key-value pairs, pick out the ones w/ 1+ occurences
        return [
            string for string, tokens in histogram.items() if tokens > 1
        ]
    
    """
     01234567890123456789012345678901
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
                           ^        ^
     CCCCCAAAAA
     histogram = {
        "AAAAACCCCC": 2,
        "AAAACCCCCA": 1,
        "AAAACCCCCC": 1,
        "AAACCCCCCA": 1,
        "AACCCCCCAA": 1,
        "AAACCCCCAA": 1,
        "AACCCCCAAA": 1,
        "ACCCCCAAAA": 1,
        "ACCCCCCAAA": 1
        "CCCCCAAAAA": 2,
        "CCCCAAAAAC": 1,
        "CCCAAAAACC": 1,
        "CCAAAAACCC": 1,
        "CAAAAACCCC": 1,
        "CCCCCCAAAA": 1,
        "CCCCAAAAAG": 1,
        "CCCAAAAAGG": 1,
        "CCAAAAAGGG": 1,
        "CAAAAAGGGT": 1,
        "AAAAAGGGTT": 1,
        "AAAAGGGTTT": 2
     }
     
     ss = "AAACCCCCAA"
     
     Time: O(n)
     Space: O(n)
    """
        