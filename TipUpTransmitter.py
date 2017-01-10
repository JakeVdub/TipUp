import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setup("XIO-P2", GPIO.OUT)
GPIO.output("XIO-P2", GPIO.HIGH)
GPIO.setup("XIO-P3", GPIO.OUT)
GPIO.setup("XIO-P5", GPIO.OUT)
GPIO.output("XIO-P3", GPIO.HIGH)
GPIO.output("XIO-P5", GPIO.HIGH)


def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("tipup")
  print("Subscribed")

def on_flag():
 # while (client.on_message == 'True'):
  GPIO.output("XIO-P2", GPIO.LOW)
  GPIO.output("XIO-P5", GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output("XIO-P5", GPIO.LOW)
  time.sleep(0.1)
  GPIO.output("XIO-P5", GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output("XIO-P5", GPIO.LOW)
  time.sleep(0.1)
  GPIO.output("XIO-P5", GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output("XIO-P5", GPIO.LOW)
  time.sleep(0.1)
  GPIO.output("XIO-P5", GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output("XIO-P5", GPIO.LOW)
  time.sleep(0.1)
  GPIO.output("XIO-P5", GPIO.HIGH)

  
def on_message(client, userdata, msg):
  print ("Message Received")
  #Try this first
  print (str(msg.payload, 'utf-8'))
  # Else try this
  #stringpayload = msg.payload.decode() #may need to be .decode('utf-8')
  #print (stringpayload)
  
  #Else:
  #
  
  if (str(msg.payload, 'utf-8') == 'flag'):
    print("Went through 'flag' if statement")
    print("Calling on_flag")   
    on_flag()
    


  if (str(msg.payload, 'utf-8') == 'off'):
    print ("Turning off LED")
    GPIO.output("XIO-P2", GPIO.HIGH)

client = paho.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.0.1", 1883)

client.loop_forever()

GPIO.cleanup()
