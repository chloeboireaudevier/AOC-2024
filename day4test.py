# Python program to search word in 2D grid in 8 directions

# This function searches for the given word
# in all 8 directions from the coordinate.
def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # return false if the given coordinate
    # does not match with first index char.
    if grid[row][col] != word[0]:
        return False

    lenWord = len(word)

    # x and y are used to set the direction in which
    # word needs to be searched.
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    # This loop will search in all the 8 directions
    # one by one. It will return true if one of the
    # directions contain the word.
    for dir in range(8):

        # Initialize starting point for current direction
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < lenWord:

            # break if out of bounds
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            # break if characters dont match
            if grid[currX][currY] != word[k]:
                break

            # Moving in particular direction
            currX += x[dir]
            currY += y[dir]
            k += 1

        # If all character matched, then value of must
        # be equal to length of word
        if k == lenWord:
            return True

    # if word is not found in any direction,
    # then return false
    return False

# This function calls search2D for each coordinate


def searchWord(grid, word):
    m = len(grid)
    n = len(grid[-1])

    ans = []

    for i in range(m):
        for j in range(n):

            # if the word is found from this coordinate,
                    # then append it to result.
            if search2D(grid, i, j, word):
                ans.append((i, j))

    return ans


def printResult(ans):
    for coord in ans:
        print(f"{{{coord[0]},{coord[1]}}}", end=" ")
    print()

file = open("inputday4.txt",'r')
content = file.readlines()
file.close()

ans = searchWord(content, 'XMAS')

print(len(ans))