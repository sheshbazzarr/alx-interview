# 0. Star Wars Characters

## Project Concept

The "0. Star Wars Characters" project requires interaction with an external API to fetch and display information about Star Wars characters based on a specified movie ID. By completing this project, you will deepen your understanding of key concepts in web programming, API interaction, and asynchronous JavaScript. This includes making HTTP requests, handling API responses, and managing asynchronous operations effectively.

## Concepts Needed

1. **HTTP Requests in JavaScript**  
   Learn to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
   - [A Complete Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)

2. **Working with APIs**  
   Understand the basics of RESTful APIs and how to interact with them, including parsing JSON data from APIs.
   - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

3. **Asynchronous Programming**  
   Learn to manage asynchronous operations in JavaScript using callbacks, promises, and async/await syntax.
   - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

4. **Command Line Arguments in Node.js**  
   Access and use command-line arguments passed to a Node.js script via the `process.argv` array.
   - [How to Parse Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/)

5. **Array Manipulation and Iteration**  
   Use JavaScript array methods to iterate over arrays and manipulate data structures, specifically for formatting and displaying character names.
   - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By familiarizing yourself with these concepts and resources, you will be able to retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, showcasing your ability to work with external APIs and handle asynchronous JavaScript code.

## Additional Resources

- [Mock Technical Interview](https://www.youtube.com/watch?v=bmqZ5AhNr3g)

## Requirements

- **Environment**: Node.js
- **Code Style**: Ensure your code follows standard JavaScript conventions.
- **Functionality**: The program must accept a movie ID as a command-line argument and display the names of characters in the movie.

# Star Wars Characters

## Project Overview

The "Star Wars Characters" project is designed to fetch and display information about Star Wars characters based on a movie ID. This program interacts with an external API to retrieve character data asynchronously, showcasing skills in API interaction, asynchronous programming, and command-line argument handling.

## Requirements

### General

- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Environment**: 
  - Files are interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
  - Ensure Node.js 10 is installed (see instructions below).
- **File Standards**:
  - All files must end with a new line.
  - The first line of each file should be exactly `#!/usr/bin/node`.
  - All files must be executable.
  - Code should comply with `semistandard` coding style (Standard + semicolons), following the AirBnB style guide.
  - Do not use `var`—use `let` or `const` instead.
  - The length of files will be tested using `wc`.
- **Modules**:
  - The `request` module is required and must be used in the program.

### Setup Instructions

#### Installing Node 10

To ensure compatibility, install Node.js version 10.x by following these steps:

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs


## Tasks

### 0. Star Wars Characters
**Mandatory**

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID (e.g., `3` for "Return of the Jedi").
- Display one character name per line in the same order as the "characters" list in the `/films/` endpoint.
- You must use the Star Wars API.
- You must use the `request` module.

**Example**

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna

