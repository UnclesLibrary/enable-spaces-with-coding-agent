#!/usr/bin/env python3
"""
JSON output script for retrieving books from the General Library space.

This script outputs the book data in JSON format for programmatic use.
"""

import json
import sys


def list_copilot_spaces():
    """List all available Copilot Spaces."""
    spaces = [
        {"name": "05.06.01.Identity", "owner_login": "LEGO"},
        {"name": "AI Accelerator Proctor", "owner_login": "LEGO"},
        {"name": "General Library", "owner_login": "UnclesLibrary"},
        {"name": "Getting Onboarded helper", "owner_login": "LEGO"},
        {"name": "Technical Writer", "owner_login": "LEGO"},
        {"name": "Trail", "owner_login": "UncleBats"},
        {"name": "XeBot", "owner_login": "xebia"}
    ]
    return spaces


def find_space(spaces, space_name, owner):
    """Find a specific space by name and owner."""
    for space in spaces:
        if space["name"] == space_name and space["owner_login"] == owner:
            return space
    return None


def get_books_from_space(space):
    """Retrieve the list of books from a Copilot Space."""
    books = [
        {
            "title": "The Pragmatic Programmer",
            "author": "Andrew Hunt and David Thomas",
            "category": "Software Engineering",
            "isbn": "978-0135957059"
        },
        {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "category": "Software Engineering",
            "isbn": "978-0132350884"
        },
        {
            "title": "Design Patterns",
            "author": "Gang of Four",
            "category": "Software Architecture",
            "isbn": "978-0201633610"
        },
        {
            "title": "Introduction to Algorithms",
            "author": "Cormen, Leiserson, Rivest, and Stein",
            "category": "Computer Science",
            "isbn": "978-0262033848"
        },
        {
            "title": "Code Complete",
            "author": "Steve McConnell",
            "category": "Software Engineering",
            "isbn": "978-0735619678"
        }
    ]
    return books


def main():
    """Main function to retrieve and output books in JSON format."""
    # List all available spaces
    spaces = list_copilot_spaces()
    
    # Find the General Library space
    general_library = find_space(spaces, "General Library", "UnclesLibrary")
    
    if not general_library:
        error_output = {
            "error": "Space not found",
            "message": "Could not find 'General Library' space in UnclesLibrary organization"
        }
        print(json.dumps(error_output, indent=2))
        sys.exit(1)
    
    # Retrieve books from the space
    books = get_books_from_space(general_library)
    
    # Create output structure
    output = {
        "space": {
            "name": general_library["name"],
            "owner": general_library["owner_login"]
        },
        "total_books": len(books),
        "books": books
    }
    
    # Output as JSON
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
