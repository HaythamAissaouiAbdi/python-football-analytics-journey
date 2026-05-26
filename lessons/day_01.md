# Day 1: Python Reboot

## Goal

By the end of today, you can run Python code, use variables, print values, and ask the user for input.

## Theory

Python runs instructions from top to bottom.

Core ideas:

- `print()` shows output.
- A variable stores a value.
- `input()` asks the user for text.
- Code becomes powerful when values can change.

## Examples

```python
name = "Haytham"
age = 16

print("Hello", name)
print("Next year you will be", age + 1)
```

```python
player = input("Player name: ")
position = input("Position: ")

print(player, "plays as a", position)
```

## Practice

Create `solutions/day_01.py` and complete these:

1. Print your name, school year, and football position.
2. Store your current average grade in a variable and print it.
3. Ask the user for their name and greet them.
4. Ask for minutes trained today and print a sentence using the answer.
5. Ask for two numbers as text, convert them with `int()`, and print their sum.

## Challenge

Build a tiny training summary program:

- Ask for player name
- Ask for training minutes
- Ask for intensity from 1 to 10
- Print a clean summary

Example:

```text
Training summary for Haytham
Minutes: 150
Intensity: 8/10
Load score: 1200
```

Load score is `minutes * intensity`.

## Reflection

At the end, update `progress_log.md` with:

- What you remembered quickly
- What confused you
- Your confidence from 1 to 10
