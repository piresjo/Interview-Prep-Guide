def minimumOnStack(operations):
    # need a return list and a stack to get the min values properly
    minList = []
    stack = []
    for operation in operations:
        # There are only three operations: push, pop, and min
        if operation == "min":
            # assuming we have something in the stack, get the min of the stack
            # (this is easy in Python so we can treat a list like a stack)
            # and add to the return list
            if stack:
                minList.append(min(stack))
        elif operation == "pop":
            if stack:
                stack.pop()
        else:
            numVal = int(operation.split(" ")[1])
            stack.append(numVal)
    return minList
