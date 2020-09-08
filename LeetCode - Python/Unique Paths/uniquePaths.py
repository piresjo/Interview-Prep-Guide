def uniquePaths(self, m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
        
    solutionMatrix = [[0] * n] * m
        
    for i in range(0, m):
        solutionMatrix[i][0] = 1
            
    for i in range(0, n):
        solutionMatrix[0][i] = 1
            
    for i in range(1, m):
        for j in range(1, n):
            solutionMatrix[i][j] = solutionMatrix[i-1][j] + solutionMatrix[i][j-1]
                
    return solutionMatrix[m-1][n-1]