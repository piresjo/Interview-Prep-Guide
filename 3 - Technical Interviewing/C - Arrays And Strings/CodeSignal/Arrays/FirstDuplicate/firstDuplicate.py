'''
Reasoning for solution:
In Python, searching in a set is O(1).
We go through the array once, so the algorithm
is O(n)
'''

def firstDuplicate(a):
    if a is None:
        return -1
    
    if len(a) < 2:
        return -1

    setVal = set() 
    for x in a:
        if x in setVal:
            return x
        setVal.add(x)
    return -1