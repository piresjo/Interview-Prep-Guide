def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    tempX = x
    reversedNum = 0

    while tempX > 0:
        digit = tempX % 10
        reversedNum = (reversedNum * 10) + digit
        tempX = tempX // 10

    return x == reversedNum
