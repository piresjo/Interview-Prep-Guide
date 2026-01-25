"""
Solution Summary:
This is similar to the Leetcode WordSearch problem.
You have to search through all of the elements in the grid.
When you find a 1, you can add that to numIslands, but you need
to process the island (i.e. find a way so that any part of that island isn't double counted).
That's where we use DFS to process the island.
Time and Space - O(rows * cols)
"""


def numIslands(grid):
    if not grid:
        return 0
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    numIslands = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "1":
                numIslands += 1
                process(i, j, grid)
    return numIslands


def process(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if grid[i][j] == "0":
        return

    grid[i][j] = "0"
    process(i + 1, j, grid)
    process(i - 1, j, grid)
    process(i, j + 1, grid)
    process(i, j - 1, grid)
