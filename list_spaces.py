#!/usr/bin/env python3
"""
Simple script to retrieve and display the General Library space information
from the UnclesLibrary organization.
"""

import json


def main():
    """
    Retrieve and display the General Library space.
    """
    # This data comes from the githubspacesmcp-list_copilot_spaces tool
    spaces = [
        {"name": "05.06.01.Identity", "owner_login": "LEGO"},
        {"name": "AI Accelerator Proctor", "owner_login": "LEGO"},
        {"name": "General Library", "owner_login": "UnclesLibrary"},
        {"name": "Getting Onboarded helper", "owner_login": "LEGO"},
        {"name": "Technical Writer", "owner_login": "LEGO"},
        {"name": "Trail", "owner_login": "UncleBats"},
        {"name": "XeBot", "owner_login": "xebia"}
    ]
    
    # Find the General Library space
    general_library = None
    for space in spaces:
        if space["name"] == "General Library" and space["owner_login"] == "UnclesLibrary":
            general_library = space
            break
    
    if general_library:
        print("=" * 60)
        print("General Library Space - UnclesLibrary Organization")
        print("=" * 60)
        print(json.dumps(general_library, indent=2))
        print("=" * 60)
    else:
        print("General Library space not found in UnclesLibrary organization")


if __name__ == "__main__":
    main()
