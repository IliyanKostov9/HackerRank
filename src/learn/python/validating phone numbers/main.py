import re
from typing import Final

PHONE_NUMBERS: list[dict[str, bool | None]] = [
    {"9587456281": True},
    {"1252478965": None},
    {"8F54698745": None},
    {"9898959398": True},
    {"879546242": None},
    {"87456985211": None},
    {"8Y45621325": None},
    {"5487F23215": None},
    {"8956324F2A": None},
    {"AFBDEG": None},
    {"879546210": None},
]

n: int = len(PHONE_NUMBERS)

REGEX: Final[str] = r"^[789]\d{9}$"

if 1 <= n <= 100:  # NOTE: 10
    for iter in range(n):
        for user_input, evaluation in PHONE_NUMBERS[iter].items():
            if 2 <= len(user_input) <= 15:
                print(user_input, end=" ")
                if evaluation == re.search(REGEX, user_input):
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")


# n: int = int(input())
# if 1 <= n <= 10:
#     for iter in range(n):
#         user_input: str = str(input())
#         if 2 <= len(user_input) <= 15:
#             if re.search(REGEX, user_input):
#                 print("YES")
#             else:
#                 print("NO")
#         else:
#             print("NO")
