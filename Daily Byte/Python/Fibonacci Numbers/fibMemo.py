def fibMemo(n: int) -> int:
    return fibHelper(n, {})
        
def fibHelper(n: int, fibonacciCache) -> int:
    if n in fibonacciCache:
        return fibonacciCache[n]
    if n == 0:
        newVal = 0
    elif n <= 2 and n > 0:
        newVal = 1
    else:
        newVal = fibHelper(n - 1, fibonacciCache) + fibHelper(n - 2, fibonacciCache)
    fibonacciCache[n] = newVal
    return newVal