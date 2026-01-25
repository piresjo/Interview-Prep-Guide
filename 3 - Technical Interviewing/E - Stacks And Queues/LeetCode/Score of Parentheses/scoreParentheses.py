def scoreOfParentheses(S):
    if not S:
        return 0
    stack = []
    score = 0
    for parenthesis in S:
        if parenthesis == "(":
            stack.append(score)
            score = 0
        else:
            score = stack.pop() + max(score * 2, 1)

    return score
