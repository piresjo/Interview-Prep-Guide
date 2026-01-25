"""General Idea:
While you can sort the abs values of the elements of the arrays, let's assume we can't do that
Instead, we'll keep track of the right and left pointers. If the abs of the left value is greater than right,
we add that to the returnList and move the left pointer accordingly. Otherwise, do it for the right value
"""


def sortedSquares(A):
    returnNumber = [0] * len(A)
    left = 0
    right = len(A) - 1
    for i in range(len(A) - 1, -1, -1):
        if abs(A[left]) > A[right]:
            returnNumber[i] = A[left] ** 2
            left += 1
        else:
            returnNumber[i] = A[right] ** 2
            right -= 1
    return returnNumber
