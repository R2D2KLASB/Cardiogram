#import random
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import maximum_filter
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 230400 , timeout=0.1)
time.sleep(3)

lst=[]
t=time.time()

loop= True
while loop:
#for i in range(0,1000):
    line = ser.readline()   # read a byte
    if line:
        string = line.decode(errors='ignore')  # convert the byte string to a unicode string
        num = int(string)
        if len(lst) > 0 and num<800:
            if num-lst[-1]>100 or num-lst[-1]>-100:# convert the unicode string to an int
                lst.append(num)
        else:
            lst.append(num)
            #print(num)
    if time.time() - t > 3:
        loop=False    
    #time.sleep(0.01)

print(len(lst))
#lst=[1,2,3,4,6,12,6,3,2,1,2,1,5,5,4,3,5,5,6,6,7,20,8,5,6,5,7,5,4,4,5,3,2,1,2,3,1,2,1,2,1,0,2,3,4,5,3,5,7,6,7,8,7,9,11,12,15,20,30,20,15,12,16,12,10,12,10,4,10,18,1,0,0,0,0,0,0,0,0]
#
# for i in range(0,100):
#     n = random.random() * 10
#     lst.append(n)
def movingAvg(LST):
    MaLst = []
    MaLst.append(LST[0])
    MaLst.append(LST[1])
    MaLst.append(LST[2])
    MaLst.append(LST[3])
    MaLst.append(LST[4])
    MaLst.append(LST[5])
    MaLst.append(LST[6])
    MaLst.append(LST[7])
    MaLst.append(LST[8])

    for i in range(9, len(LST), 1):
        MA = (LST[i] + LST[i-1] + LST[i-2] + LST[i-3] + LST[i-4]+LST[i-5] + LST[i-6] + LST[i-7] + LST[i-8] + LST[i-9]) / 10
        MaLst.append(int(MA))
    return MaLst


minimum = min(lst)
for i in range(len(lst)):
    lst[i] -= minimum

maximum = max(lst)
for i in range(len(lst)):
    lst[i] *= (25000/maximum)
MaLsT = movingAvg(lst)

    
print(MaLsT[50])
MaLst = movingAvg(MaLsT)
measurements=[]
for i in range(0,len(lst),1):
    measurements.append(i * 15)

plt.plot(measurements,MaLst, label = "Moving average(5)")#, linestyle="-.")

# put your data here
data = np.array(lst)

filter_win_size = 15
peak_intensity_threshold = 6

max_data = maximum_filter(data, filter_win_size)
min_data = -maximum_filter(-data, filter_win_size)

# select places where we detect maximum but not minimum -> we dont want long plateaus
peak_mask = np.logical_and(max_data == data, min_data != data)
# select peaks where we have enough elevation
peak_mask = np.logical_and(peak_mask, max_data - min_data > peak_intensity_threshold)
# a trick to convert True to 1, False to -1
peak_mask = peak_mask * 2 - 1
# select only the up edges to eliminate multiple maximas in a single peak
peak_mask = np.correlate(peak_mask, [-1, 1], mode='same') == 2

max_places = np.where(peak_mask)[0]


gcodelist =[measurements, MaLst]
def listToGcode(list):
    f = open("heartbeat.gcode", "w")

    for i in range(len(list[0])):
        x = str(list[0][i])
        y = str(list[1][i])
    
        f.write("G1 X" + x + " Y"+ y + " ;\n")
    f.close()
listToGcode(gcodelist)



fig, ax = plt.subplots()
r = range(data.shape[0])
ax.plot(r, data, 'k')
ax.plot(max_places, data[max_places], 'xr')
ax.grid()
ax.axis((0, len(lst), min(lst), max(lst)))
plt.show()

