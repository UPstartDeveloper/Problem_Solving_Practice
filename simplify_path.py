"""
def simplifyPath(path):
    # split by /
    split_by_slash = path.split('/')
    # init canonical list
    canon = list()
    # iterate and add important tokens
    for token in split_by_slash:
	    if len(token) > 0:
	        # go back up a level
	        if len(canon) > 0 and token == '..':
                canon.pop(-1)
	        # go down a level
            else:  # we have a new directory to go down to
                canon.append(token)     
    # join the paths
    SLASH = '/'
    path = SLASH
    for index, token in enumerate(canon):
        path += token
        # add slashes for all token other than the last
        if index < len(canon) - 1:
            path += SLASH
    return path
"""

def simplifyPath(path):
  # place chars for simplified version in a stack
  canon_path = list(['/'])
  # iterate over the path
  index = 1
  while index < len(path):
    # get the symbol at this index
    char = path[index]
    # directories to remove
    if char == '.':
      if len(canon_path) > 0:
        canon_path.pop()
    elif (char == '/' and canon_path[-1] == '/'):
        pass
    # characters to add
    else:
      canon_path.append(char)
    # move on to the next char
    index += 1
  # convert list to a string - remove the trailing / if needed
  if len(canon_path) > 1:
    return ''.join(canon_path[:-1])
  else:
    return ''.join(canon_path)
    
  
"""
path
/home//foo/

canon_path
/home/
"""
   
 
if __name__ == '__main__':
    testPath = "/a/./b/../../c/"
    testResult = simplifyPath(testPath)
    print(testResult)


"""
split_by_slash                        |  canon            |  path
['a', 'b', 'c', 'd', '.', '.', '..']  | ['a', 'b', 'c',]  | '/a/b/c


"""