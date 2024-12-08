def island_perimeter(grid):
    """Returns the perimeter of an island described by a grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check top, left, right, and bottom cells
                if r == 0 or grid[r - 1][c] == 0:  # Top
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Bottom
                    perimeter += 1

    return perimeter

