# enable-spaces-with-coding-agent

This repository contains a script to retrieve the list of books from the "General Library" space in the UnclesLibrary organization.

## Usage

Run the script to retrieve and display the book list:

```bash
python3 retrieve_books.py
```

## Output

The script will:
1. Search for available Copilot Spaces
2. Locate the "General Library" space in the UnclesLibrary organization
3. Retrieve and display the list of books with details (title, author, year, category)
4. Output the results in both human-readable format and JSON format

## Example Output

```
📚 Books from General Library Space (UnclesLibrary)
================================================================================

Total books found: 5

1. The Pragmatic Programmer
   Author: Andrew Hunt, David Thomas
   Year: 1999
   Category: Software Engineering

2. Clean Code
   Author: Robert C. Martin
   Year: 2008
   Category: Software Engineering

...
```

## Requirements

- Python 3.6 or higher
