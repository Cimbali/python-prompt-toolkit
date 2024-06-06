#!/usr/bin/env python3
from prompt_toolkit import prompt

if __name__ == "__main__":
    answer = prompt("Give me some input: ", wrap_lines=False, multiline=True)
    print(f"You said: {answer}")
