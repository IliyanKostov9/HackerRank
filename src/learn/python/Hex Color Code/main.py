# n: int = int( input() )

import re
from typing import Final


input = """
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
"""

# input: list[str] = []
n: int = 20
REGEX: Final[str] = r"^(#?=([0-9]{3,6}[a-e][A-E]))$"
if 0 < n < 50:
    # for iter in range(n):
    #     input.append(str(input()))

    hex_codes: list[str] = re.findall(REGEX, input, flags=re.MULTILINE)
    print("".join(hex_codes))
