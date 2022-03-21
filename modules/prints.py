"""
    All prints to be printed at specific time.
    Prints made by @MTraveller
    https://github.com/MTraveller
"""
from subprocess import run
from time import sleep
from art import tprint
from modules.slow_print import sprint

BINARY = (
    "01001001 00100000 01101000 01101111 "
    "01110000 01100101 00100000 01111001 "
    "01101111 01110101 00100000 01100101 "
    "01101110 01101010 01101111 01111001 "
    "00100000 01010111 01100101 01100010 "
    "01100001 01101100 01111001 01111010 "
    "01100101 01110010 00100000 01100001 "
    "01110011 00100000 01101101 01110101 "
    "01100011 01101000 00100000 01100001 "
    "01110011 00100000 01001001 00100000 "
    "01100101 01101110 01101010 01101111 "
    "01111001 01100101 01100100 00100000 "
    "01101101 01100001 01101011 01101001 "
    "01101110 01100111 00100000 01101001 "
    "01110100 00100000 00111010 00101001 "
    "\n")

YES_NO = ("Please use '\x1b[1;32my\x1b[0;0m' "
          "for \x1b[1;32mYes\x1b[0;0m, "
          "'\x1b[1;31mn\x1b[0;0m' for \x1b[1;31mNo\x1b[0;0m "
          "or '\x1b[1;95mquit\x1b[0;0m' to \x1b[1;95mQuit\x1b[0;0m the app")


WEBALYZER = (
    "Webalyzer is an app that asks for a URL "
    "and returns the requested data.",
    "It first checks the answer of the input, "
    "validates the input, and continues.\n",
    "Webalyzer first confirms if the answer is "
    "a link with HTTP(s), domain, and TLD.",
    "Then it moves on to validate the link by requesting "
    "the host,", "and if the response header is 200, "
    "then it carries on to the actual feature.\n",
    "The features of Webalyzer is:\n",
    "1. Validate the standard META TAGs of:",
    "https://html.spec.whatwg.org/"
    "multipage/semantics.html#standard-metadata-names\n",
    "2. Validate HTML, CSS, and Javascript",
    "Validation of HTML, CSS is through 'W3C' "
    "=> World Wide Web Consortium",
    "Validation of Javascript is through CodeBeautify\n",
)

CHOICES = [
    "==============================",
    "  Please Choose By (Number)   ",
    "==============================",
    "\\*  (1): Validate HTML      */",
    "/*       -------------      *\\",
    "\\*  (2): Validate CSS       */",
    "**       -------------      **",
    "/*  (3): Validate JS        *\\",
    "==============================",
]

WRONG = "\x1b[1;31mWrong answer, please try again...\x1b[0;0m"


BYE_TOP = [
    "╔" + ("╦" * 78) + "╗",
    "║" + ("║" * 78) + "║",
    "║" + ("║" * 78) + "║",
    "╠" + ("╩" * 78) + "╣",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
]

BYE_BRAND = [
    "║" + (" " * 12) + " _      __        __          __" + (" " * 34) + "║",
    "║" + (" " * 12) +
    "| | /| / / ___   / /  ___ _  / /  __ __ ___ ___   ____" +
    (" " * 12) + "║",
    "║" + (" " * 12) +
    "| |/ |/ / / -_) / _ \\/ _ `/ / /  / // //_ // -_) / __/" +
    (" " * 12) + "║",
    "║" + (" " * 12) +
    "|__/|__/  \\__/ /_.__/\\_,_/ /_/   \\_, / /__/\\__/ /_/" +
    (" " * 15) + "║",
    "║" + (" " * 44) +
    "/___/              " + (" " * 15) + "║",
]

BYE_MIDDLE = [
    "║" + (" " * 78) + "║",
    "║" + (" " * 78) + "║",
    "║" + (" " * 17) +
    "We thank you for your visit and hope to see" + (" " * 18) + "║",
    "║" + (" " * 22) + "you soon again :) Have a great day." +
    (" " * 21) + "║",
    "║" + (" " * 78) + "║",
]

BYE_BOTTOM = [
    "║" + (" " * 78) + "║",
    "╠" + ("╦" * 78) + "╣",
    "║" + ("║" * 78) + "║",
    "║" + ("║" * 78) + "║",
    "╚" + ("╩" * 78) + "╝",
]

QUITORNEW = ("Did you know;\nTyping '\x1b[1;95mquit\x1b[0;0m'"
             " or '\x1b[1;94mnew\x1b[0;0m' any time,\n"
             "will \x1b[1;95mQuit\x1b[0;0m the app or"
             " validate a \x1b[1;94mNew\x1b[0;0m URL ;)")


def print_yes_no():
    """
        Prints "yes / no / quit" above input
    """

    sprint(YES_NO)


def print_brand_name():
    """
        Prints brand name
    """

    tprint("Webalyzer", font="Small Slant", sep="\n")


def print_intro_welcome():
    """
        Prints welcome intro
    """

    tprint("Welcome to", font="Small Slant", sep="\n")
    sleep(.02)
    print_brand_name()
    sleep(.5)


def print_about():
    """
        Prints Webalyzer's short story
    """

    for line in WEBALYZER:
        sleep(1)
        print(line)


def run_choices_screen():
    """
        Prints run_choices options
    """
    print(QUITORNEW)
    print()
    for line in CHOICES:
        print(line)
    print()


def print_outro():
    """
        Prints Webalyzer's Outro
    """

    run('clear', check=True)
    for line in BYE_TOP + BYE_BRAND + BYE_MIDDLE + BYE_BOTTOM:
        sleep(.02)
        print(line)
