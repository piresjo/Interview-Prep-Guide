def containsDuplicates(a):
    if not a:
        return False
    return len(a) != len(set(a))
