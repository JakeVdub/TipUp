import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


LED1 = 17
LED2 = 27
Buzzer = 22


def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("tipup")
  print("Subscribed")
  LED1 = 17
  LED2 = 27
  Buzzer = 22
   
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(LED1, GPIO.OUT)
  GPIO.setup(LED2, GPIO.OUT)
  GPIO.setup(Buzzer, GPIO.OUT)
  GPIO.output(LED1, GPIO.LOW)
  GPIO.output(LED2, GPIO.LOW)
  GPIO.output(Buzzer, GPIO.LOW)

def on_flag(number):
 # while (client.on_message == 'True'):
  if (number == 1):
    GPIO.output(LED1, GPIO.HIGH)
  else:
    GPIO.output(LED2, GPIO.HIGH)

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
  time.sleep(0.15) 
  GPIO.output(Buzzer, GPIO.LOW)
  time.sleep(0.1)

def on_message(client, userdata, msg):
  print ("Message Received")
  print (str(msg.payload, 'utf-8'))
  
  if (str(msg.payload, 'utf-8') == 'flag'):
    print("Went through 'flag' if statement")
    print("Calling on_flag")
    on_flag(1)

  if (str(msg.payload, 'utf-8') == 'flag2'):
    print("Went through 'flag' if statement")
    print("Calling on_flag")
    on_flag(2)

  if (str(msg.payload, 'utf-8') == 'off'):
    print ("Turning off LED")
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    
  if (str(msg.payload, 'utf-8') == 'stealth'):
    print ("Silencing Buzzer")
    GPIO.output(Buzzer, GPIO.LOW)
           
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.1", 1883)

client.loop_forever()

GPIO.cleanup()

