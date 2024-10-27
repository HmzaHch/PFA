from machine import Pin, I2C, SoftI2C
import time
import urequests
from i2c_lcd import I2cLcd 



    


# Firebase Realtime Database URL
FIREBASE_URL = "https://fir-app-bd76d-default-rtdb.firebaseio.com/test/password.json"
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

def get_all_keys_pressed():
  """
  Function to continuously read and store all pressed keys until "#" is pressed
  """
  pressed_keys = ""
  while True:
    key = read_key()
    if key is not None:
      pressed_keys += key
      time.sleep(0.3)
      if key == "#":
        return pressed_keys

def connect_to_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wifi.isconnected():
        pass
    print("Connected to Wi-Fi")

def get_password_from_firebase():
    response = urequests.get(FIREBASE_URL)
    password = response.text  # Retrieve the response text
    return password

# Main function (modified)
def main():
  """
  Main function to read and print all keys pressed until "#"
  
  """
  AddressOfLcd = 0x27
  i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
# connect scl to GPIO 22, sda to GPIO 21
  lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)
  print("Press keys on the keypad (press # to finish)...")
  pressed_keys = get_all_keys_pressed()
  print("All keys pressed:", pressed_keys)
  password = get_password_from_firebase()
  print("Password retrieved from Firebase:", password)
  if(password==pressed_keys):
      lcd.putstr('acces accepted');
    else:
        lcd.putstr('acces denied');
      

if __name__ == "__main__":
  main()
