import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setup("XIO-P0", GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup("XIO-P2", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

client = paho.Client()
client.connect("172.20.0.1", 1883)

print ("CONNECTED")
while True:
  if (GPIO.input("XIO-P0") == False):
    print ("Button P0 Pressed")
    client.publish('tipup', 'flag')
    time.sleep(1)

  if (GPIO.input("XIO-P2") == False):
    print ("Button P2 Pressed")
    client.publish('tipup', 'off')
    time.sleep(1)

