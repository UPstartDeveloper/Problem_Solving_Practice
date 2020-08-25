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
   
 
if __name__ == '__main__':
    testPath = "/a//b////c/d//././/.."
    testResult = simplifyPath(testPath)
    print(testResult)


"""
split_by_slash                        |  canon            |  path
['a', 'b', 'c', 'd', '.', '.', '..']  | ['a', 'b', 'c',]  | '/a/b/c


"""