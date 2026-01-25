def backspaceCompare(S, T):
    finalS = ""
    finalT = ""

    for i in range(0, len(S)):
        if S[i] == "#":
            if i == 0:
                continue
            else:
                finalS = finalS[:-1]
        else:
            finalS += S[i]

    for i in range(0, len(T)):
        if T[i] == "#":
            if i == 0:
                continue
            else:
                finalT = finalT[:-1]
        else:
            finalT += T[i]

    return finalT == finalS
