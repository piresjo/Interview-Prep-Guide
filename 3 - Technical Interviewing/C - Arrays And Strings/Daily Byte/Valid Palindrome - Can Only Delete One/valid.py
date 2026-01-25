def isPalindromeRange(s, i, j):
    return all(s[k] == s[j - k + i] for k in range(i, j))


def validPalindrome(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            return isPalindromeRange(s, i + 1, j) or isPalindromeRange(s, i, j - 1)
    return True
