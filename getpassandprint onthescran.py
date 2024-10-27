import network
import urequests
from time import sleep_ms, ticks_ms , time
from machine import I2C, Pin , SoftI2C
from i2c_lcd import I2cLcd 

AddressOfLcd = 0x27
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
# connect scl to GPIO 22, sda to GPIO 21
lcd = I2cLcd(i2c, AddressOfLcd, 2, 16)
# Wi-Fi credentials
WIFI_SSID = "."
WIFI_PASSWORD = "1929394959"

# Firebase Realtime Database URL
FIREBASE_URL = "https://fir-app-bd76d-default-rtdb.firebaseio.com/password.json"



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

def main():
    connect_to_wifi()
    password = get_password_from_firebase()
    print("Password retrieved from Firebase:", password)
    lcd.move_to(0,0)
    lcd.putstr(password)

if __name__ == "__main__":
    main()