# Word Search

## Problem

Given a 2D array of letters (`board`) and a string `word`, determine if there is a path on the `board` that gives us the `word`

## Things To Note

## Solution Explained

We're using graph traversal principles for this. We can think of the grid (a 2D array) as a graph.
Because you're looking for a word (which is a string of contiguous letters), we'll be doing DFS on the grid until we get the word (or can't get a word through that path)

You have to search through all of the elements in the grid. When you find a letter that matches the first letter of the word, you have to run DFS to ensure the rest of the word can be found.
When you search, you have to make sure you don't double count letters.
However, you have to find a way for that letter to be found in another search, so some temp variables will be needed.

For readability, the DFS here will be recursive.

## Solution

```python
def exist(board, word):
    if board is None or word is None:
        return False
    if len(board) == 0 or len(board[0]) == 0:
        return False
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            # If you find the starting letter of the word
            if board[i][j] == word[0] and search(i, j, 0, board, word):
                return True
    return False
    
def search(i, j, count, board, word):
    # Return if count == len(word). This means we found the entire word
    if count == len(word):
        return True
        
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
        return False
        
    # Keep the tempVal
    tempVal = board[i][j]
    # Make empty, so letters don't get double counter
    board[i][j] = ""
    # Recurse
    found = search(i + 1, j, count + 1, board, word) or search(i - 1, j, count + 1, board, word) or search(i, j + 1, count + 1, board, word) or search(i, j - 1, count + 1, board, word)
    # Since that letter is needed for other searches, we need to put the letter back
    board[i][j] = tempVal
    return found
```

## Analysis

In the worst case, all elements of the grid are examined. The worst grid, both for space and time, is a completely filled in board (i.e. all rows have the same number of elements).
This leads to both a recursive stack that is `rows * columns` large, and `rows * columns` elements are exampled. Therefore, we can say that both time and space complexity is `O(rows * columns)`