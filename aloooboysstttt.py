from machine import Pin
from machine import  ADC
import time
import network

ssid = '.'
password = '1929394959'
flame_pin = 22
#gaz_pin = 5

# Create an ADC instance (if required by your library)
adc = ADC (Pin(5))
adc.atten(ADC.ATTN_11DB)  # Adjust attenuation if needed


# Set pin modes (optional)
flame_sensor = Pin(flame_pin, Pin.IN)
vent_gaz = Pin(21, Pin.OUT)  # Assuming vent control

def connect(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    while not station.isconnected():
        pass
    print('Connection successful')

connect(ssid, password)


def read_flame_sensor():
    flame_value = flame_sensor.value()
    if flame_value == 1:
        print("Flame detected!")
        print(flame_sensor.value())
    else:
        print("No flame detected.")
        print(flame_sensor.value())
        
    # Implement logic for LED control based on flame value
    # ...

def read_gaz_sensor():
   gazp_value = adc.read()
   if gazp_value < 200:
      vent_gaz.value(1)  # Activate vent if gas value is low
    else:
       print("Non gaz detection")

while True:
    read_gaz_sensor()
    time.sleep(2)
    read_flame_sensor()
    time.sleep(2)