# `Minimum Operations`

This project contains a Python script that calculates the minimum number of operations required to result in exactly `n` H characters in a file.

## Problem Description

In a text file, there is initially a single character 'H'. Your text editor can execute only two operations in this file:

1. Copy All
2. Paste

Given a number `n`, the task is to calculate the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Solution

The solution is implemented in the `minOperations` function, which uses the following approach:

1. If `n` is less than 2 or not an integer, return 0 (no operations needed).
2. Find the prime factors of `n`.
3. The sum of these prime factors gives the minimum number of operations.

### Helper Function: `factors`

The `factors` function is used to find the prime factors of a given number:

- It first checks for factors of 2.
- Then it checks for odd factors up to the square root of the number.
- If any factor remains after this process, it's added to the list.

## Usage

