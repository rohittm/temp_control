import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial('/dev/ttyACM0',9600)
s = 0
in1 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, False)

try:
    while True:
        read_serial= float(ser.readline())
        s+=1
        print "Old Temprature: "+str(int(read_serial))
    
        if read_serial>=21:
            GPIO.output(in1, True)
            time.sleep(0.1)
            GPIO.output(in1, False)
            print "Lower Temprature by: "+str(int(read_serial)-21)+" degrees(C)"
        else:
            print "It's already too cold! :)"
    
except KeyboardInterrupt:
    GPIO.cleanup()