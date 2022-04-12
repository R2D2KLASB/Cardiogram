import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import maximum_filter
import serial
import time
import random

ser = serial.Serial('/dev/ttyUSB0', 230400 , timeout=0.1)


def readSerial():
    t=time.time()
    while True:
        line = ser.readline()   # read a byte
        if line:
            string = line.decode(errors='ignore')       # convert the byte string to a unicode string
            num = int(string)
            if len(lst) > 0 and num<800:
                if num-lst[-1]>100 or num-lst[-1]>-100: # convert the unicode string to an int
                    lst.append(num)
            else:
                if num < 1000:
                    lst.append(num)
        if time.time() - t > 3:     # 3 second measurement
            break  

def movingAvg(LST):             # Moving average of 10
    MaLst = []
    MaLst.append(int(LST[0]))
    MaLst.append(int(LST[1]))
    MaLst.append(int(LST[2]))
    MaLst.append(int(LST[3]))
    MaLst.append(int(LST[4]))
    MaLst.append(int(LST[5]))
    MaLst.append(int(LST[6]))
    MaLst.append(int(LST[7]))
    MaLst.append(int(LST[8]))

    for i in range(9, len(LST), 1):
        MA = (LST[i] + LST[i-1] + LST[i-2] + LST[i-3] + LST[i-4]+LST[i-5] + LST[i-6] + LST[i-7] + LST[i-8] + LST[i-9]) / 10
        MaLst.append(int(MA))
    return MaLst

def scale():
    minimum = min(lst)
    for i in range(len(lst)):
        lst[i] -= minimum

    maximum = max(lst)
    for i in range(len(lst)):
        lst[i] *= (25000/maximum)
    

def listToGcode(list):
    f = open("heartbeat.gcode", "w")

    for i in range(len(list[0])):
        x = str(list[0][i])
        y = str(list[1][i])
    
        f.write("G01 X" + x + " Y"+ y + "\n")
        
    f.write("G00 X0 Y0")
    f.close()


while True:
    if readbutton: #moet nog gedaan worden
        try:
            lst=[]
            time.sleep(3)
            readSerial()
            scale()
            MovingAvg10 = movingAvg(lst)
            MovingAvg100 = movingAvg(MovingAvg10)
            XCoordinates=[]
            for i in range(0,len(lst),1):
                XCoordinates.append(i * 15)
            gcodelist =[XCoordinates, MovingAvg100]
            listToGcode(gcodelist)
        except:
            sendPicture(random.randint(12)) #functie moet nog gemaakt worden
