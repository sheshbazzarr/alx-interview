#!/usr/bin/python3
"""
0-main.py
This script tests the island_perimeter function with various test cases.
"""

island_perimeter = __import__('0-island_perimeter').island_perimeter

def run_test_cases():
    test_cases = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 4),  # Single land cell
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),  # Entire grid is water
        ([[1, 1], [1, 1]], 8),                   # Full land grid
        ([[0, 1, 1, 1, 0]], 8),                  # Single row of land
        ([[0], [1], [1], [1], [0]], 8),          # Single column of land
        ([[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 12),  # Complex island shape
        ([[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]], 8),  # Disconnected land (invalid input edge case)
        ([[1, 0], [0, 0]], 4),                   # Single cell at the edge
        ([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]], 12),  # Large rectangular island
        ([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]], 16),  # Multiple layers
    ]

    for i, (grid, expected) in enumerate(test_cases, start=1):
        result = island_perimeter(grid)
        print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'} | Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_test_cases()
