class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        LeetCode: https://leetcode.com/problems/simplify-path/
        
        Input/Problem:
            str
            immutable
            abs path
            
            //// = /
            
            > 2 x "." ===> file/dir name
        
        Output:
            abs path
            
        Intuition:
            stacks
            trees
            
        EC:
        
            1) invalid path --> ValueError
            
            2) multiple slashes --> replace w/ "/"
            
            > 2 x "." ===> include it 
            
                "/home/zain..../foo/"
                "/home/..../foo/"
                ---> "/home/zain..../foo"
                
                
        Approach:
        
        "/home//foo/".split("/")
        
        --> ["home", "", "foo"]
        --> ["home", -1, "foo"]
        
            1) parse the abs path
                split it by "/"
                on the output list
                    delete "" --> mark it as SKIP
                    remove single "." --> SKIP
                    
            2) gather all the dirs
                canonical_path = cp = []
                traverse output:
                    if dir_or_file_ --> not int
                        and not == ".."
                            add to the end of cp
                        and if it's == ".." and len(cp) > 0:
                            pop the last added elem
                            
            3) return output as a str --> "/".join(cp)
                
                        
        
        """
        ### HELPERS
        def _parse(path):
            # split it by "/"
            parsed_path = pp = path.split("/")
            for index, path_obj in enumerate(parsed_path):
                # mark it as SKIP
                if len(path_obj) == 0 or path_obj == ".":
                    parsed_path[index] = 0
            return parsed_path
                
        def _convert_abs_to_canonical(parsed_path):
            canonical_path = cp = []  # our "stack"
            # traverse output:
            for path_obj in parsed_path:
                # if dir_or_file_ --> check if not int
                if isinstance(path_obj, str) is True:
                    # and not == ".."
                    if path_obj != "..":
                        cp.append(path_obj)
                    # and if it's == ".." and len(cp) > 0:
                    elif len(cp) > 0:
                        cp.pop()     
            return cp
                        
        ### MAIN
        # 1) parse the abs path
        parsed_path = _parse(path)  
                    
        # 2) gather all the dirs
        canonical_path = cp = _convert_abs_to_canonical(parsed_path)
                            
        # 3) final conversion --> str
        pre_canonical_path = ["/", "/".join(cp)]  
        return "".join(pre_canonical_path)
