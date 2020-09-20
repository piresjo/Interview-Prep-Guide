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