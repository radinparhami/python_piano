from keyboard import on_release, wait
from random import randint
from winsound import Beep

inp = input(
    'Enter the frequency,'
    ' just press enter to randomize :  '
)

rnd = (lambda key_code: randint(37, 32767 // key_code))
check = (lambda fr: rnd(100) if fr > 32767 else fr)

try:
    assert not inp or 100 <= int(inp) <= 500
except AssertionError:
    print(
        "The data should not be less than 100"
        " and greater than 500."
    )

on_release(
    lambda event: Beep(
        event.scan_code *
        check(
            inp and int(inp) or
            rnd(event.scan_code)
        ),
        100
    )
), wait()
