# Python program to Print all possible paths from top left to bottom right of a mXn matrix

allPaths = []


def findPaths(grid, m, n):
    path = [0 for d in range(m+n-1)]
    findPathsUtil(grid, m, n, 0, 0, path, 0)


def findPathsUtil(grid, m, n, i, j, path, indx):
    global allPaths
    # if we reach the bottom of grid, we can only move right
    if i == m-1:
        for k in range(j, n):
            # path.append(grid[i][k])
            path[indx+k-j] = grid[i][k]
            # if we hit this block, it means one path is completed.
            # Add it to paths list and print
            print(path)
            allPaths.append(path)

            return

# if we reach to the right most corner, we can only move down
    if j == n-1:
        for k in range(i, m):
            path[indx+k-i] = grid[k][j]
        # path.append(grid[j][k])
        # if we hit this block, it means one path is completed.
        # Add it to paths list and print
        print(path)
        allPaths.append(path)
        return

    # add current element to the path list
    # path.append(grid[i][j])
    path[indx] = grid[i][j]

    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(grid, m, n, i+1, j, path, indx+1)

    # move down in y direction and call findPathsUtil recursively
    findPathsUtil(grid, m, n, i, j+1, path, indx+1)


if __name__ == '__main__':
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    findPaths(grid, 3, 3)
    # Minimum using sum()
    print(min(allPaths, key=sum))
