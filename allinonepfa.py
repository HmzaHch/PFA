from machine import Pin,ADC
import time
import network


//variables 	
ssid ='.'
password ='1929394959'
flame_pin = 22
gaz_pin= 23
servo_gaz= 
vantulo_gaz=Pin(12,Pin.OUT)



def connect(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())
  


connect(ssid, password)

flame_sensor = Pin(flame_pin, Pin.IN)
def read_flame_sensor():
    flame_value = flame_sensor.value()
    led=Pin(19,Pin.OUT)
    if flame_value == 1:
        print("detectation de flamée")
    else:
        print("non flame detection")
        


def read_gaz_sensor():
    gaz=ADC(Pin(gaz_pin))
    gaz.atten(ADC.ATTN_11DB)
    gaz_value=gaz.read()
    if(gaz_value<200):
        vantulo_gaz.value(1)
    else:
        print("non gaz detectation")




    









