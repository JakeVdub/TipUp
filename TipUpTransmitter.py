import paho.mqtt.client as paho
import CHIP_IO.GPIO as GPIO
import time

GPIO.cleanup()

LED1 = "XIO-P2"
LED2 = "XIO-P3"
Buzzer = "XIO-P5"

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)
GPIO.output(Buzzer, GPIO.HIGH)


def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("tipup")
  print("Subscribed")

def on_flag():
 # while (client.on_message == 'True'):
  GPIO.output(LED1, GPIO.LOW)
  GPIO.output(Buzzer, GPIO.LOW)
  time.sleep(0.1)
  GPIO.output(Buzzer, GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output(Buzzer, GPIO.LOW)
  time.sleep(0.1)
  GPIO.output(Buzzer, GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output(Buzzer, GPIO.LOW)
  time.sleep(0.1)
  GPIO.output(Buzzer, GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output(Buzzer, GPIO.LOW)
  time.sleep(0.1)
  GPIO.output(Buzzer, GPIO.HIGH)

def on_message(client, userdata, msg):
  print ("Message Received")
  print (str(msg.payload, 'utf-8'))
  
  if (str(msg.payload, 'utf-8') == 'flag'):
    print("Went through 'flag' if statement")
    print("Calling on_flag")
    on_flag()

  if (str(msg.payload, 'utf-8') == 'off'):
    print ("Turning off LED")
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(Buzzer, GPIO.HIGH)
    
  if (str(msg.payload, 'utf-8') == 'stealth'):
    print ("Silencing Buzzer")
    GPIO.output(Buzzer, GPIO.HIGH)
           
client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("172.20.0.1", 1883)

client.loop_forever()

GPIO.cleanup()

