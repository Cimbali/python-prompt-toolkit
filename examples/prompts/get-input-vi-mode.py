#!/usr/bin/env python3
from prompt_toolkit import prompt

if __name__ == "__main__":
    print("You have Vi keybindings here. Press [Esc] to go to navigation mode.")
    answer = prompt("Give me some input: ", multiline=False, vi_mode=True)
    print(f"You said: {answer}")
