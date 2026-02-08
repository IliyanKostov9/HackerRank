regex_pattern = (
    r"^(?!MMMM)(?!.*(?:M.*M.*M.*M.*M|I.*I.*I.*I|L.*L|X.*X.*X.*X))[MDXCVLI]+$"
)

import re

roman_numbers_list: list[dict[str, bool]] = [
    {"DXXVIIII": False},
    {"CDXXI": True},
    {"MMMM": False},
    {"MMMDCCCLXXXXVIII": False},
    {"MMMDCCCLXXXVIII": True},
    {"MMMCMXCIX": True},
    {"DCCCLXX": True},
    {"LL": False},
    {"MMMCDVIII": True},
]

for roman_numbers_dict in roman_numbers_list:
    for number, evaluated in roman_numbers_dict.items():
        print(
            f"Roman letter {number} is evaluated as: {str(bool(re.match(regex_pattern, number)) == evaluated)}"
        )
