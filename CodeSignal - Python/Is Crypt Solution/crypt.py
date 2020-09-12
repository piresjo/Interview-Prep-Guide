def isCryptSolution(crypt, solution):
    # solution dict and number dict
    # for easy retrieval of both, since we need to add the numerical values 
    # of the first two elements, then convert that sum to letters
    solDict = {}
    numDict = {}
    for x in solution:
        solDict[x[0]] = x[1]
        numDict[x[1]] = x[0]
        
    # check for leading zeroes
    for word in crypt:
        if len(word) > 1 and solDict[word[0]] == '0':
            return False
    
    # Get the numerical values of the codes for the first two strings
    answerString1 = ""
    answerString2 = ""
    for char in crypt[0]:
        answerString1 += solDict[char]
    
    for char in crypt[1]:
        answerString2 += solDict[char]
        
    # Getting the sum for the third word
    answerString3 = str(int(answerString1) + int(answerString2))

    # Check if the numbers match the code for the third string
    if len(answerString3) != len(crypt[2]):
        return False
        
    for i in range(0, len(answerString3)):
        if answerString3[i] not in numDict:
            return False
        if numDict[answerString3[i]] != crypt[2][i]:
            return False 
        
    
    return True