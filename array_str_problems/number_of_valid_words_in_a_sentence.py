from string import ascii_lowercase


class Solution:
    def countValidWords(self, sentence: str) -> int:
        """
        LeetCode: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
        
        Input:
            char set:
                - lowercase English (case-sensitive)
                - "-"
                - ! . , (not "?"")
                - spaces (however many is fine)
            
            space speratated tokens
            
            ASSUME: .split()
        
        Output:
            int - # of tokens
        
        Intuition:
            rule-checking
            
        EC:
            - multiple spaces ---> tokens must start w/ letters
            - empty - N/A --> 0
            - TODO
        
        Approach:
        
            A: split the string into space-separated substrings
            
            B: validate the list of subs
                1) for each char in substr:
                    - is it in the char set?
                    - have we reach our hyphen_limit?
                        - is it surrounded by letters?
                    - is there 0 or (1 at the end) punc?
                1) if valid --> count += 1

            C: return count
            
        
        
        """
        ### HELPERS
        def _is_valid(sub: str) -> bool:
            """fail fast rule checking logic"""
            punc_count = pc = 0
            hypen_count = hc = 0
            # 1) for each char in substr:
            for index in range(len(sub)):
                char = sub[index]
                # - is it in the char set?
                if char.isnumeric():  # 10 iteration
                    return False
                elif char in ascii_lowercase:
                    continue
                elif char == "-":
                    if hc < 1:
                        # - is it surrounded by letters?
                        if 0 < index < len(sub) - 1:
                            if (sub[index - 1] in ascii_lowercase) and (
                                sub[index + 1] in ascii_lowercase
                            ):
                                hc += 1
                                continue
                    return False
                # - is there 0 or (1 at the end) punc?
                elif char in [".", ",", "!"]:
                    if pc < 1 and index == len(sub) - 1:
                        continue
                    else:
                        return False
            # all checks pass
            return True

        ### DRIVER
        # A: split the string into space-separated substrings
        substrings = sentence.split()
        # B: validate the list of subs
        count = 0
        for sub in substrings:
            if _is_valid(sub) is True:
                count += 1
        return count
