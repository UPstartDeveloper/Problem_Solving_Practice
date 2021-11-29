from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Leetcode: 
          https://leetcode.com/problems/accounts-merge/
          
        Input/Problem:
            list of accounts
            first cols - first names (just English, lower + upper)
            jagged matrix
            >= 1 valid unique email in acct
            
            merge - same first name, >= 1 common email ----> mergesort the unique
            
            ASSUME immutable
            ASSUME name comp - case sensitive
            
        Output:
            return the merged accts - any order
            
        Intuition:
            set - intersection
            sorting - built-in sort
            
        EC:
            TODO
            
        Approach:
            
            1) DIY
                1) Check if there is a merge needed:
                    hashmap the 1st col - see if dupe names - {name: [row_indices]}
                    if not ----> return input
                2) if dupe names ---> merging:
                    init output = []
                    
                    make merges:
                        if name has 1 row - sort emails, put in the output
                        if > 1 row:
                            disjoint set - so init all emails that belong together
                            make a 2D list -- cast as a list, sort, add the name at beginning
                            extend output by each merged acct in the 2D list
                
                3) return output        
        
        Example:
            [["John","johnsmith@mail.com","john_newyork@mail.com"],
             ["John","johnsmith@mail.com","john00@mail.com"],
             ["Mary","mary@mail.com"],
             ["John","johnnybravo@mail.com"]]
             
        {
            John: [0, 1, 3]
            Mary: [2]
        }
        
        ["John","johnsmith@mail.com","john_newyork@mail.com"], 
        ["John","johnsmith@mail.com","john00@mail.com"],       
        ["John","johnnybravo@mail.com"]  <
        
        buckets =  [
            {"johnsmith@mail.com","john_newyork@mail.com", "john00@mail.com"} Jogn
            {johnnybravo@mail.com"}
        ]
        """
        ### HELPERS
        def _merge(rows):
            # A: disjoint set - so init all emails that belong together
            merged = m = list()
            name, email_sets = rows[0][0], [
                set(r[1:]) for r in rows
            ]
            # B: combining sets of emails together
            for es in email_sets:
                # first see if it belongs in an older set
                does_belong = False
                for index, b in enumerate(merged):
                    if len(b & es) > 0:
                        merged[index] = b.union(es)
                        does_belong = True
                if does_belong is False:  # add new bucket
                    merged.append(es)  
            # C: make a 2D list -- cast as a list, sort, add the name at beginning
            for index, es in enumerate(merged):
                email_list = sorted(list(es))
                email_list.insert(0, name)
                merged[index] = email_list
            # D: done!
            return merged 
        
        ### DRIVER
        # 1) Check if there is a merge needed - TODO
        name_rows = dict()
        for index, acct in enumerate(accounts):
            name = acct[0]
            if name not in name_rows:
                name_rows[name] = [index]
            else:  # seen before
                name_rows[name].append(index)
        # 2) if dupe names ---> merging:
        output = list()
        for name, rows_indices in name_rows.items():
            # extend output by each merged acct in the 2D list
            rows = [accounts[row_index] for row_index in rows_indices]
            output.extend(_merge(rows))                
        # 3) return output     
        return output
