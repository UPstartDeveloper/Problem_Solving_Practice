from collections import deque

def simplifyPath(path):
    """Converts a UNIX-style file path to its canonical version.

       Parameters:
       path(str): a file path to a certain directory, may been seen on 
                  Linux or Mac OSX.
       
       Returns: str: the canonical form of path
    
    Assumptions:
    - the path is mutable 
    - the path always begins with a leading slash

    Complexity:
    O(n) time, because we iterate over all characters in the path string
    O(1) space, because we reuse all the letters in string, and add no extra
    """
    # place chars for simplified version in a stack
    path = deque(path)
    canon_path = list()
    # iterate over the path
    while len(path) > 0:
        # get the symbol at the start
        char = path.popleft()
        # flag for when to stop if/else logic
        check_again = True
        # directories to remove
        if char == '.':
            if len(canon_path) > 0:
                canon_path.pop()
                check_again = False
        # characters to skip
        elif char == '/':
            if len(canon_path) > 0 and canon_path[-1] == '/':
                check_again = False
        # characters to add
        if check_again == True:
            canon_path.append(char)
    # convert list to a string - remove the trailing / if needed
    if len(canon_path) > 1:
        return ''.join(canon_path[:-1])
    else:
        return ''.join(canon_path)
    

if __name__ == '__main__':
    testPath = "/a/./b/../../c/"
    testResult = simplifyPath(testPath)
    print(testResult)
