def addBinary(a, b):
    # For ease in going through a and b
    # make a and b into stacks
    a, b = list(a), list(b)
    carry = 0
    ans = ""
    while a or b or carry:
        # first, we pop and add to the carry
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        # using divmod, we can get both the carry and the remainder
        # remainder gets added to the answer string
        # carry gets carried over
        carry, remain = divmod(carry, 2)
        ans += str(remain)
    return ans[::-1]