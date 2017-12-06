import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

sensor = "XIO-P0"
stealthSwitch = "XIO-P2"
flagLight = "XIO-P4"

stealth = False
flagDown = False

GPIO.cleanup()
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stealthSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(flagLight, GPIO.OUT)
GPIO.output(flagLight, GPIO.HIGH)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  time.sleep(1)
  #After connection is established begin looking for flags
  while True:
    if (GPIO.input(sensor) == False):
      print ("Flag is Up")
      flagDown = False
      client.publish('tipup', 'flag')
      time.sleep(10)
      
    if (GPIO.input(sensor) == True):
      print ("Flag is Down")
      if (flagDown == False):
        client.publish('tipup', 'off')
        flagDown = True;
        time.sleep(1)

    if (GPIO.input(stealthSwitch) == False):
      if (stealth == False):
        print ("Silencing Beeper")
        client.publish('tipup', 'stealth')
        stealth = True
        time.sleep(1)
      
    if (GPIO.input(stealthSwitch) == True):
      if (stealth == True):
        stealth = False
      
      

client = paho.Client()
client.on_connect = on_connect

client.connect("172.20.0.1", 1883)
time.sleep(1)
client.loop_forever()





