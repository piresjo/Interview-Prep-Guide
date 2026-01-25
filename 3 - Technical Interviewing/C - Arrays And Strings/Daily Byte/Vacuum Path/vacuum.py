"""General Idea:
If the vacuumer is back in place, it's horizontalDistance and verticalDistance from starting
point should both be zero. So, set up horizontalDistance and verticalDistance values, have them increase
when going right/up, and have them decrease when going left/down.
"""


def vacuum(strVal):
    horizontalDistance = 0
    verticalDistance = 0
    for char in strVal:
        if char == "L":
            horizontalDistance -= 1
        elif char == "R":
            horizontalDistance += 1
        elif char == "U":
            verticalDistance += 1
        else:
            verticalDistance -= 1

    return horizontalDistance == 0 and verticalDistance == 0
