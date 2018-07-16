import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)


GPIO.output(13,False)
GPIO.output(19,False)
GPIO.output(26,False)


while True:
   
    
# loop when heater active -Green light
     x=GPIO.input(6)
     print(str(x))
     if int(x) == 0:
        print ("Heater Active")
        GPIO.output(13,True)
        GPIO.output(19,False)
        GPIO.output(26,True)


# when coolant active -red light active
     else :
        print("Coolant Active")
        GPIO.output(13,False)
        GPIO.output(19,True)
        GPIO.output(26,False)

GPIO.cleanup()
