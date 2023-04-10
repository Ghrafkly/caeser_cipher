import logging
import sys


def encoder(char_pt: chr, shift: int) -> str:
    # Throw error if char is not on the ANSI keyboard layout
    for char in char_pt:
        if ord(char) < 32 or ord(char) > 126:
            logging.error(f"Incorrect symbol '{char}':{ord(char)} for conversion")
            sys.exit()

    for i, char in enumerate(char_pt):
        """
        Hold the value of the ascii value of char + the shift value.
        If the ASCII value of hold exceeds 126, subtract 95. This
        ensures that it loops back to the start (32).
        """
        hold = ord(char) + shift

        if hold > 126:
            hold -= 95

        char_pt[i] = chr(hold)

    return char_pt
