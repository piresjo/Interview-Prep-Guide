def stairs(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    answerArray = [-1] * (n+1)
    answerArray[0] = 1
    answerArray[1] = 1
    answerArray[2] = 2
    
    for i in range(3, n+1):
        answerArray[i] = answerArray[i-1] + answerArray[i-2] + answerArray[i-3]
    
    return answerArray[n]
