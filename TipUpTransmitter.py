import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO

GPIO.cleanup()
GPIO.setup("XIO-P2", GPIO.OUT)
GPIO.output("XIO-P2", GPIO.HIGH)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("tipup")
  
def on_message(client, userdata, msg):
  print (str(msg.payload))
  message = msg.payload
  print(userdata)
  print(client)
  print (message.length)

  if (message =="b'flag'"):
    print("passed if statement")
    #This is where the CHIP will turn on the LED
    # Could also just use two different messages instead of checking
    #   the client id...
    GPIO.output("XIO-P2", GPIO.LOW)

  if (msg.payload == "off"):
    GPIO.output("XIO-P2", GPIO.HIGH)

client = paho.Client()
client.connect("localhost", 1883)

client.on_connect = on_connect
client.on_message = on_message

#client.publish("tipup", "flag")

client.loop_forever()

GPIO.cleanup()
