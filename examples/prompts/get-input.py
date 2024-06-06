#!/usr/bin/env python3
"""
The most simple prompt example.
"""

from prompt_toolkit import prompt

if __name__ == "__main__":
    answer = prompt("Give me some input: ")
    print(f"You said: {answer}")
