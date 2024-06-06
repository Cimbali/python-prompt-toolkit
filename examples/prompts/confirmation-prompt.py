#!/usr/bin/env python3
"""
Example of a confirmation prompt.
"""

from prompt_toolkit.shortcuts import confirm

if __name__ == "__main__":
    answer = confirm("Should we do that?")
    print(f"You said: {answer}")
