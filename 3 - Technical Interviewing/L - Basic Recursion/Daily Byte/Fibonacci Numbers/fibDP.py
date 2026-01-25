def fibDP(n: int) -> int:
    if n == 0:
        return 0
    fibCache = []
    fibCache.append(0)
    fibCache.append(1)
    for i in range(2, n + 1):
        fibCache.append(fibCache[-1] + fibCache[-2])
    return fibCache[n]
