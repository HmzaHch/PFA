import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect(".", "1929394959")

while not GLOB_WLAN.isconnected():
  pass

#firebase example
import ufirebase as firebase
firebase.setURL("https://fir-app-bd76d-default-rtdb.firebaseio.com/")

#Put Tag1
firebase.put("test/password", "303031", bg=0)
firebase.put("test/dht11/humid", 15, bg=0)
#Get Tag1
firebase.get("test/password", "var1", bg=0)
print("password: "+str(firebase.var1))
#Get Tag1
firebase.get("test/dht11/temp", "var2", bg=0)
print("temp: "+str(firebase.var2))
#Get Tag1
firebase.get("test/dht11/humid", "var3", bg=0)
print("humidity: "+str(firebase.var3))
#Get Tag1
firebase.get("test/door", "var4", bg=0)
print("door statue : "+str(firebase.var4))
#Get Tag1
firebase.get("test/fireValue", "var5", bg=0)
print("Fire Value: "+str(firebase.var5))
#Get Tag1
firebase.get("test/gazValue", "var6", bg=0)
print("Gaz Value: "+str(firebase.var6))
#Get Tag1
firebase.get("test/led", "var7", bg=0)
print("led Statue: "+str(firebase.var7))


#Do something in this time
while 1:
  print(end=".")
  MOD_TIME.sleep(.100)
  try: 
    firebase.lolwhat
    break
  except:
    pass