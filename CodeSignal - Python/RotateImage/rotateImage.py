def rotateImage(a):
    # Make checks for faulty images
    if len(a) == 0:
        return None
    if len(a[0]) != len(a):
        return None
        
    lenVal = len(a)
    
    # Since we're going layer by layer, and all these images
    # are square, we only need to go halfway to touch all layers
    for layer in range(0, lenVal // 2):
        firstVal = layer
        lastVal = lenVal - 1 - layer
        
        for i in range(firstVal, lastVal):
            offset = i - firstVal
            top = a[firstVal][i]
            a[firstVal][i] = a[lastVal-offset][firstVal]
            a[lastVal-offset][firstVal] = a[lastVal][lastVal-offset]
            a[lastVal][lastVal-offset] = a[i][lastVal]
            a[i][lastVal] = top
            
    return a