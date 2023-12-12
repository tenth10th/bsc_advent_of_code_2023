import string
from typing import List, Iterable

"""
Some stuff we talked about:

[] = square braces, or square brackets or just brackets
() = Parenthesis or just parens
{} = curly braces or just curlies

x = foo(y)  # "assign x to the foo of y"

Callable: Things that can be called, e.g. foo()
    Functions, also Class Methods
    x = Foo()
    x.bar()

{} = Dictonary literals {"foo": 1} or Set literals {1, 2}

[] = Accessing by index [0] or key ["foo"]

-> = "arrow operator", or sometimes "indirect"

from collections import abc
    Abstract Base Classes - Make it easy to create
    your own List or Dictionary-like objects...
"""


def main(lines: Iterable[str]) -> int:
    numbers = list()
    for line in lines:
        numbers.append(parse_line(line))
    return sum(numbers)


def parse_line(line: str) -> int:
    first_digit = ""
    last_digit = ""

    for character in line:
        if character in string.digits:
            first_digit = character
            break

    for character in reversed(line):
        if character in string.digits:
            last_digit = character
            break

    # print("First digit:", first_digit)
    # print("Last digit:", last_digit)

    string_number = first_digit + last_digit

    # print("number:", repr(string_number))

    actual_number = int(string_number)

    return actual_number


def load_lines_from_file() -> List[str]:
    with open("data/day_1_data.txt", "r") as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    """
    Ensure that the code only runs if call this file directly
    e.g. `python src/main.py`
    """
    lines = load_lines_from_file()
    total = main(lines)
    print("total:", total)
