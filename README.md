# enable-spaces-with-coding-agent

A tool to retrieve books from the "General Library" Copilot Space in the UnclesLibrary organization.

## Overview

This repository provides functionality to connect to GitHub Copilot Spaces and retrieve a list of books from the "General Library" space owned by UnclesLibrary.

## Features

- List all available GitHub Copilot Spaces
- Find and connect to the "General Library" space
- Retrieve and display books from the library
- Formatted output showing book titles, authors, and categories

## Usage

### Human-Readable Output

Run the book retrieval script:

```bash
python3 retrieve_books.py
```

The script will:
1. List all available Copilot Spaces
2. Locate the "General Library" space in UnclesLibrary
3. Retrieve the books from the space
4. Display them in a formatted list

### JSON Output

For programmatic use, you can get the books in JSON format:

```bash
python3 retrieve_books_json.py
```

This outputs structured JSON data that can be piped to other tools or parsed by scripts.

### Example Output

**Human-Readable Format:**

```
GitHub Copilot Spaces - Book Retrieval Tool
======================================================================

Step 1: Listing available Copilot Spaces...
Found 7 spaces

Step 2: Looking for 'General Library' space in UnclesLibrary...
✓ Found: General Library (owned by UnclesLibrary)

Step 3: Retrieving books from the space...

======================================================================
Books in the General Library (4 total)
======================================================================

1. The Pragmatic Programmer
   Author: Andrew Hunt and David Thomas
   Category: Software Engineering

2. Clean Code
   Author: Robert C. Martin
   Category: Software Engineering
...
```

**JSON Format:**

```json
{
  "space": {
    "name": "General Library",
    "owner": "UnclesLibrary"
  },
  "total_books": 5,
  "books": [
    {
      "title": "The Pragmatic Programmer",
      "author": "Andrew Hunt and David Thomas",
      "category": "Software Engineering",
      "isbn": "978-0135957059"
    },
    ...
  ]
}
```

## Requirements

- Python 3.x
- Access to GitHub Copilot Spaces (through MCP server)

## Technical Details

The implementation uses:
- GitHub MCP Server integration for Copilot Spaces
- Space listing and identification
- Book data retrieval and formatting

## Future Enhancements

- Integration with actual GitHub Copilot Spaces API when `get_copilot_space` tool becomes available
- Support for filtering books by category
- Export books to different formats (JSON, CSV, Markdown)
- Search functionality within the library

## Notes

The current implementation includes demonstration data. To retrieve actual books from the Copilot Space, the `get_copilot_space` MCP tool or direct GitHub Copilot Spaces API access would be required.
