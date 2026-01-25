def sudoku2(grid):
    if grid is None:
        return False
    return checkSubgrid(grid) and checkRows(grid) and checkCols(grid)


def checkSubgrid(grid):
    for i in range(0, 3):
        for j in range(0, 3):
            gridSet = set()
            for x in range(i * 3, (i * 3) + 3):
                for y in range(j * 3, (j * 3) + 3):
                    if grid[x][y] != ".":
                        if grid[x][y] in gridSet:
                            return False
                        gridSet.add(grid[x][y])
    return True


def checkRows(grid):
    for rows in grid:
        checkRow = [x for x in rows if x != "."]
        checkSet = set(checkRow)
        if len(checkRow) != len(checkSet):
            return False
    return True


def checkCols(grid):
    for col in range(0, len(grid[0])):
        colSet = set()
        for row in range(0, len(grid)):
            if grid[row][col] != ".":
                if grid[row][col] in colSet:
                    return False
                colSet.add(grid[row][col])
    return True
