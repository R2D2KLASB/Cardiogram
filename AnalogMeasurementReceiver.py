import serial
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

import XYtoGcode

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

reading = False
waiting = True

heartTime = 0
listX = []
listY = []

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
def receiveHeartBeat():
    while True:
        while waiting:
            if GPIO.input(10) == GPIO.HIGH:
                reading = True
                waiting = False
                heartTime = 0


        while reading:
            heartTime = 0
            starttime = time.time()
            while time.time()-starttime < 3:
                line = ser.readline()   # read a byte
                if line:
                    string = line.decode()  # convert the byte string to a unicode string
                    num = int(string) # convert the unicode string to an int
                    listX.append(heartTime * 8)
                    listY.append(num * 50)
                    heartTime += 1 #TODO max need to be determined

            XYtoGcode.listToGcode([listX,listY])
            listX.clear()
            listY.clear()
            waiting = True
            reading = False

ser.close()