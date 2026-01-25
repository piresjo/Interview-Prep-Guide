def stairs(n):
    if n < 2:
        return 1

    answerArray = [-1] * (n + 1)
    answerArray[0] = 1
    answerArray[1] = 1

    for i in range(2, n + 1):
        answerArray[i] = answerArray[i - 1] + answerArray[i - 2]

    return answerArray[n]
