import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO

GPIO.cleanup()
GPIO.setup("XIO-P2", GPIO.OUT)
GPIO.output("XIO-P2", GPIO.HIGH)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("tipup")
  print("Subscribed")
  
def on_message(client, userdata, msg):
  print ("Message Received")
  print (str(msg.payload))
  
  if (msg.payload == 'flag'):
    print("Went through 'flag' if statement")
    print("Turning on LED")   
    GPIO.output("XIO-P2", GPIO.LOW)

  if (msg.payload == "off"):
    print ("Turning off LED")
    GPIO.output("XIO-P2", GPIO.HIGH)

client = paho.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.0.1", 1883)

client.loop_forever()

GPIO.cleanup()
