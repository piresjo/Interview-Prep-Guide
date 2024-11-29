'''
    General Idea: You need to get the max left boundary for each section
    and the max right boundary for each section. So, create two arrays to house
    the left and right heights. leftHeights[0] = heights[0] and 
    rightHeights[len(heights)-1] = heights[len(heights)-1]. For the left heights,
    we'll see if the height of the section is bigger than the current max left
    boundary, and update as appropriate. Similar thing happens to the right.

    However, to correctly determine the trapped rainwater, we need to get
    the min between the right and left max boundaries for each section 
    (as a visualization, if a bucket has a left side that's two inches high and
    a right side that's four inches, the water going past the two inches will
    overflow). We also need to subtract the height of the region we're at, since
    obviously rain can't be trapped there.
'''

def trap(height):
    if height is None:
        return 0
        
    if len(height) == 0:
        return 0
        
    leftHeights = [0] * len(height)
    rightHeights = [0] * len(height)
        
        
    leftHeights[0] = height[0]
    for i in range(1, len(height)):
        leftHeights[i] = max(leftHeights[i-1], height[i])
        
    rightHeights[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, -1, -1):
        rightHeights[i] = max(rightHeights[i+1], height[i])
            
    stored = 0
        
    for i in range(0, len(height)):
        stored += min(leftHeights[i], rightHeights[i]) - height[i]
            
    return stored