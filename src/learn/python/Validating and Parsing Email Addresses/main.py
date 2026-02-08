import re
from typing import Final


# n: int = input()

n: int = 2

EMAILS: Final[list[str]] = ["DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>"]
REGEX: Final[str] = r"^(\w)\s<([\w\-_]*@\w\.\w{3})>$"

if 0 < n < 100:
    for iter in range(n):
        # user_input: str = input()

        for user_input in EMAILS:
            if match := re.search(REGEX, user_input):
                print(match.group())
