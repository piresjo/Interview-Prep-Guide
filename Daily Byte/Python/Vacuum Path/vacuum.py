def vacuum(strVal):
    horizontalDistance = 0
    verticalDistance = 0
    for char in strVal:
        if char == 'L':
            horizontalDistance -= 1
        elif char == 'R':
            horizontalDistance += 1
        elif char == 'U':
            verticalDistance += 1
        else:
            verticalDistance -= 1

    return horizontalDistance == 0 and verticalDistance == 0