def simplifyPath(path):
    simplifiedPath = []
    for directory in path.split('/'):
        if directory == '.':
            continue
        elif directory == '..':
            if len(simplifiedPath) != 0:
                simplifiedPath.pop()
        else:
            if directory:
                simplifiedPath.append(directory)
    
    returnVal = "/" + "/".join(simplifiedPath)
    return returnVal