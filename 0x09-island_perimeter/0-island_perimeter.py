#!/usr/bin/python3
"""island_perimeter Module"""


def island_perimeter(grid):
    """
    calculate the perimeter of a single island in a grid,
    where the grid is represented by a 2D array of integers
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell is land (1)
            if grid[i][j] == 1:
                # Count the number of adjacent water cells (0s)
                # Up
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Down
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
