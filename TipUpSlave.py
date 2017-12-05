import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

sensor = "XIO-P0"
stealthSwitch = "XIO-P2"
flagLight = "XIO-P4"

stealth = False
flag-down = False

GPIO.cleanup()
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stealthSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(flagLight, GPIO.OUT)
GPIO.output(flagLight, GPIO.HIGH)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  
  #After connection is established begin looking for flags
  while True:
    if (GPIO.input(sensor) == False):
      print ("Flag is Up")
      flag-down = False
      client.publish('tipup', 'flag')
      time.sleep(10)
      
    if (GPIO.input(sensor) == True):
      print ("Flag is Down")
      if (flag-down == False):
        client.oublish('tipup', 'off')
        flag-down = True;

    if (GPIO.input(stealthSwitch) == False):
      if (stealth == False):
        print ("Silencing Beeper")
        client.publish('tipup', 'stealth')
        stealth = True
      
    if (GPIO.input(stealthSwitch) == True):
      if (stealth == True):
        stealth = False
      
      

client = paho.Client()
client.on_connect = on_connect

client.connect("172.20.0.1", 1883)
client.loop_forever()





