import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

arr = [14,15,18,23,24]

while True:
    for x in range(0,5,1):
        GPIO.output(arr[x],0)
    for i in range (5,0,-1):
        for j in range(0,i,1):
            GPIO.output(arr[j],1)
            time.sleep(1)
            if (j<i-1):
                GPIO.output(arr[j],0)