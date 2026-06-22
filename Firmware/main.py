# Hi my name is Amogh and this is my code

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()


# Apparently you can use this instead of that rows and columns things for simpler macropads!
keyboard.matrix = KeysScanner(
    pins=[board.D10, board.D9, board.D8],
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.Z)]
]

if __name__ == "__main__":
    keyboard.go()