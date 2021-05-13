class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        in == out in len
        
        empty string
        
        2-9 ONLY
        
        in order for sure
        
        Intutiom: ==> want all the perm
        
        Approach:
        
        1. Four nested loops
          - init out == []
          
            - check for the digit
            - iterate through digit_letter combos
            - once a full perm --> out
            
         - return out
         # --------------------------
         {
            "2": ["a", "b", "c"]
            "3": ["d", "e", "f"]
         }
        
        o = ["ad", "ae", "af", "bd"]
        
        1st --- ["a", "b", "c"]
                       ^
        2nd --> ["d", "e", "f"]
                  ^
        
        [
            ["a", "b", "c"],
            ["d", "e", "f"]
        ]
        Edge Cases:
        "" --> []
        spaces --> N/A
        1 or 0 --> N/A
        
        """
        def recursive_helper(list_index, all_letters, current_perm, all_perms):
            if len(list_index) < len(all_letters):
                # get the list of letters
                list_letters = all_letters[list_index]
                # iterate through all of those
                for letter in list_letters:  # [a, b, c]
                    current_perm.append(letter)  # [a]
                    # check the length of the permutation so far
                    if len(current_perm) == len(digits):
                        full_perm = "".join(current_perm)
                        all_perms.append(full_perm)
                        current_perm.pop()
                        #current_perm = []
                    # for the very last list of letters
                    # if list_index == len(all_letters) - 1:

                    # moving --> last list of letters
                    else: 
                        recursive_helper(list_index + 1, all_letters, 
                                         current_perm, all_perms)
            current_perm = []
        
        def form_perms(digits, digit_letters):
            
            if len(digits) == 0:
                return []
            
            # A: gather up all the letter for the perms
            all_letters = list()
            for digit in digits:
                all_letters.append(digit_letters[digit])
                
            # B: init current permutations, and a list to store all
            all_perms = []
            current_perm = []
            
            # C: form the perms
            # total_num_perms = 3 ** len(digits)
            
            # while len(all_perms) < total_num_perms:
            list_index = 0
            recursive_helper(list_index, all_letters, current_perm, all_perms)
            
            """"
            23
            all_letters = [  
                       l
                ["a", "b", "c"],  <--- ll, 1st 
                ["d", "e", "f"] <-- ll, 2nd
            ]
            
            all_perms = [ad, ]
            current_perm = [a, d], []
            
            list_index = 0
            
            
            
            
            
            
            
            
            ############################
            
            
            
            
            
            
        
            for list_letters in all_letters:
                for letter in list_letters:
                    # adds the next letter
                    current_perm.append(letter)
                    # check the length of the permutation so far
                    if len(current_perm) == len(digits):
                        full_perm = "".join(current_perm)
                        all_perms.append(full_perm)
                        current_perm = []
                    else:
                        bre
            """
            
            return all_perms
                        
            """
            23
            all_letters = [  
                       l
                ["a", "b", "c"],  <--- ll
                ["d", "e", "f"]
            ]
            
             all_perms = []
            current_perm = []
            
            
            ############################
            digits = "2"
            
            all_letters = [
                ll = ["a", "b", "c"]
                            l
            ]
            
            all_perms = ["a", "b", ]
            current_perm = [b]
            fp = "a"
            
            """
        
        # A: TODO: digit --> letter mappings 
        digit_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "b", "c"],
            "7": ["a", "b", "c"],
            "8": ["a", "b", "c"],
            "9": ["a", "b", "c"],
        }
        # B: form all the perms 
        perms = form_perms(digits, digit_letters )
        # C: return the perms
        return perms
        