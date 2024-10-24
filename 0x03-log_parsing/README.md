# Log Parsing

This project involves creating a script that parses log data from stdin, computes metrics, and prints statistics.

## Task Description

Write a script that reads stdin line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: `File size: <total size>`
    where `<total size>` is the sum of all previous `<file size>`
  - Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
    - If a status code doesn't appear or is not an integer, don't print anything for this status code
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

## Usage


200: 2


200: 2