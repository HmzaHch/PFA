from machine import Pin, I2C
from machine import ADC
import time
import network
from i2c_lcd import I2cLcd 
ssid = '.'
password = '1929394959'


# Define the pins connected to the rows and columns of the keypad
# Adjust these pin numbers according to your wiring
ROWS = [32, 33, 25, 26]
COLS = [27, 14, 12, 13]

# Define the mapping of keys on the keypad
# This corresponds to the key layout of a standard 4x4 matrix keypad
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Initialize the pins for rows as inputs with pull-up resistors
row_pins = [Pin(pin_num, Pin.IN, Pin.PULL_UP) for pin_num in ROWS]

# Initialize the pins for columns as outputs
col_pins = [Pin(pin_num, Pin.OUT) for pin_num in COLS]

def read_key():
    """
    Function to read the currently pressed key on the keypad
    """
    for i, col_pin in enumerate(col_pins):
        # Set one column pin low at a time
        col_pin.value(0)

        # Check which row pin is low (indicating a key press)
        for j, row_pin in enumerate(row_pins):
            if row_pin.value() == 0:
                # Calculate the corresponding key based on the row and column indices
                key = keys[j][i]
                return key

        # Reset the column pin back to high
        col_pin.value(1)

    return None



def lcd_print(ch):
    DEFAULT_I2C_ADDR= 0x20
    # Initialize I2C bus
    i2c = SoftI2C(scl=Pin(5), sda=Pin(4),freq=400000)

# Initialize the LCD
    lcd = LCD(i2c, DEFAULT_I2C_ADDR, 2, 16)

    lcd.putstr(ch);















def connect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass
    print('Connection successful')

connect(ssid, password)







def main():
    """
    Main function to continuously read and print key presses
    """
    print("Press a key on the keypad...")
    while True:
        key += read_key()
        if key is not None:
            print("Key pressed:", key)
        time.sleep(0.2)  # Add a small delay to debounce the keypad

if __name__ == "__main__":
    main()








