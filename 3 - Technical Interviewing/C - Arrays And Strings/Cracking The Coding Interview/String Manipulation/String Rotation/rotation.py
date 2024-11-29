def rotation(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return s2 in s1s1
    return False