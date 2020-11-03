def isTreeIdentical(t, s):
    if not t and not s:
        return True
    if not t or not s:
        return False
    return identical(t, s)
    
def identical(t, s):
    if not t and not s:
        return True
    if not t or not s:
        return False
        
    if t.value == s.value:
        return identical(t.left, s.left) and identical(t.right, s.right)
        
    return False

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None