import re
from typing import Final


# n: int = int(input())


EMAILS: Final[list[str]] = [
    "DEXTER <dexter@hotmail.com>",
    "VIRUS <virus!@variable.:p>",
    "dheeraj <dheeraj-234@gmail.com>",
    "crap <itsallcrap>",
    "harsh <harsh_1234@rediff.in>",
    "kumal <kunal_shin@iop.az>",
    "mattp <matt23@@india.in>",
    "harsh <.harsh_1234@rediff.in>",
    "harsh <-harsh_1234@rediff.in>",
    "shashank <shashank@9mail.com>",
    "shashank <shashank@gmail.9om>",
    "shashank <shashank@gma_il.com>",
    "shashank <shashank@mail.moc>",
    "shashank <shashank@company-mail.com>",
    "shashank <shashank@companymail.c_o>",
    "vineet <vineet.iitg@gmail.com>",
    "vineet <vineet.iitg@gmail.co>",
    "vineet <vineet.iitg@gmail.c>",
]

REGEX: Final[str] = r"^(\w+)\s<([a-z][\w\-_\.]+@[a-z]+\.[a-z]{1,3})>$"
n: int = len(EMAILS)

if 0 < n < 100:
    for iter in range(n):
        # user_input: str = input()

        if match := re.search(REGEX, EMAILS[iter]):
            print(match.group())
