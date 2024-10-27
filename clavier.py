from keyboard import Keyboard
from machine import Pin

# Define the key matrix
MATRIX = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Define the row and column pins of the keypad
ROW_PINS = [Pin(32), Pin(33), Pin(25), Pin(26)]
COL_PINS = [Pin(27), Pin(14), Pin(12), Pin(13)]

# Create a Keyboard instance
kb = Keyboard(rows=ROW_PINS, cols=COL_PINS, keys=MATRIX)

# Main loop to continuously read keypresses
while True:
    key = kb.getch()
    if key is not None:
        print("Key pressed:", key)
