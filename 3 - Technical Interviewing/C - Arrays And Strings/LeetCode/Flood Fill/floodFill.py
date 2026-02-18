from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    stack = []
    stack.append((sr, sc))
    originalColor = image[sr][sc]
    if color == originalColor:
        return image

    while len(stack) != 0:
        coordinates = stack.pop()
        if image[coordinates[0]][coordinates[1]] != originalColor:
            pass
        else:
            image[coordinates[0]][coordinates[1]] = color

            if coordinates[0] > 0:
                stack.append((coordinates[0] - 1, coordinates[1]))
            if coordinates[0] < len(image) - 1:
                stack.append((coordinates[0] + 1, coordinates[1]))
            if coordinates[1] > 0:
                stack.append((coordinates[0], coordinates[1] - 1))
            if coordinates[1] < len(image[0]) - 1:
                stack.append((coordinates[0], coordinates[1] + 1))

    return image
