
# 0x05. N Queens

## Project Concept

The **“0x05. N Queens”** project is a classic problem in computer science and mathematics, known for applying the **backtracking algorithm** to place **N non-attacking queens** on an **N×N chessboard**. Successfully completing this project requires a solid understanding of key concepts and the use of resources to grasp the necessary algorithms and techniques.

### Key Concepts

1. **Backtracking Algorithms**
   - Understanding backtracking to explore all potential solutions and backtrack when a solution path is unsuccessful.
   - [Introduction to Backtracking](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)

2. **Recursion**
   - Using recursive functions to implement backtracking algorithms.
   - [Recursion in Python](https://realpython.com/python-thinking-recursively/)

3. **List Manipulations in Python**
   - Creating and manipulating lists, particularly for storing the positions of queens on the board.
   - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

4. **Python Command Line Arguments**
   - Handling command-line arguments with Python’s `sys` module.
   - [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

By studying these concepts and utilizing the resources provided, you will gain the knowledge required to implement an efficient solution to the N queens problem using Python. This project tests programming and problem-solving skills while offering an opportunity to develop algorithmic thinking and optimization techniques.

### Additional Resources
- **Mock Interview**: Gain insight and practice your skills.
  - [Mock Interview Video](https://www.youtube.com/watch?v=GneS80iYa7I)

## Requirements

### General
- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Environment**: All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3 (version 3.4.3)**
- **File Formatting**:
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
- **Project Structure**:
  - A `README.md` file, located at the root of the project folder, is mandatory
- **Coding Standards**:
  - Code should follow **PEP 8** style guidelines (version 1.7.*)
- **Executable Files**: All files must be executable


The **N queens puzzle** is a classic problem in computer science and mathematics that involves placing **N non-attacking queens** on an **N×N chessboard**. This project leverages the **backtracking algorithm** to explore potential solutions efficiently.

### Task: N Queens

In this task, you will write a program that solves the **N queens problem**.

### Requirements
- **Usage**: `nqueens N`
- If the program is called with the wrong number of arguments, it should print:
followed by a new line, and exit with status `1`.
- **N** must meet the following criteria:
- **N** is an integer greater than or equal to 4.
- If **N** is not an integer, print:
  ```
  N must be a number
  ```
  followed by a new line, and exit with status `1`.
- If **N** is less than 4, print:
  ```
  N must be at least 4
  ```
  followed by a new line, and exit with status `1`.

### Output
- The program should output every possible solution to the N queens problem.
- Each solution is displayed as a list of lists where each inner list represents the position `[row, column]` of a queen.
- Solutions do not need to be printed in a specific order.

### Example Usage
```bash
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

