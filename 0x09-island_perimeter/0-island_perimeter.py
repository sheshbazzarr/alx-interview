#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.

    Args:
        grid (list of list of int): 2D grid representation of the island and water.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four directions
                if i == 0 or grid[i-1][j] == 0:  # Top
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right
                    perimeter += 1
    return perimeter

