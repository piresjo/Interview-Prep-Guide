'''
    Solution Summary:
    You have to search through all of the elements in the grid.
    When you find a letter that matches the first letter of the word, you have to run DFS
    to ensure the rest of the word can be found.
    When you search, you have to make sure you don't double count
    However, you have to find a way for that letter to be found in another search
    Time and Space - O(rows * cols)
'''

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
