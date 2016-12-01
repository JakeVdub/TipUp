import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setup("XIO-P0", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup("XIO-P2", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


client = paho.Client()
client.connect("172.20.0.1", 1883)
#client.on_connect = on_connect
#client.on_publish = on_publish
#client.on_disconnect = on_disconnect

#client.connect("172.20.0.1", 1883)

#def on_connect(mosq, obj, rc): 
print ("CONNECTED")
while True:
  if (GPIO.input("XIO-P0") == False):
    print ("Shit this button actually works..")
    time.sleep(1)
    client.publish('tipup', 'flag')

  if (GPIO.input("XIO-P2") == False):
    print ("And this one does too motherfucker")
    time.sleep(1)
    client.publish('tipup', 'off')


#def on_publish(mosq, obj, mid):
 # print ("JUST PUBLISHED")


#client.connect("172.20.0.1", 1883)
