#!/usr/bin/env python3
from prompt_toolkit import prompt

if __name__ == "__main__":
    password = prompt("Password: ", is_password=True)
    print(f"You said: {password}")
