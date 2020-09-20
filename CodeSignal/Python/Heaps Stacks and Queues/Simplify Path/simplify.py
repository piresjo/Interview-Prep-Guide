def simplifyPath(path):
    # Use a stack, since the navigation of levels in a file system best mimics the push and pop 
    # of stacks
    simplifiedPath = []
    # The path is a string, but we can get the directories by splitting by '/'
    for directory in path.split('/'):
        if directory == '.':
            # We don't have to do anything, so continue
            continue
        elif directory == '..':
            # in this case, we're going up a level, so we can pop and go up a level in
            # the file system heirarchy
            if len(simplifiedPath) != 0:
                simplifiedPath.pop()
        else:
            # we're going into a new directory, so we should push into the stack
            if directory:
                simplifiedPath.append(directory)
    
    # regenerate into a string
    returnVal = "/" + "/".join(simplifiedPath)
    return returnVal