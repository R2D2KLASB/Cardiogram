import random
from matplotlib import pyplot as plt

def detectAPeak(number1,number2,number3):
    global ChangeValueInProcent
    peak = False
    change = number2 - number1
    changeInProcent = abs((change * 100) / (number2 + 0.000001)) # + 0.000001 in case number2 is 0, division by zero is not allowed
    if changeInProcent >= ( ChangeValueInProcent ) and number3 < number2 and number1 < number2:
     #^^verschil in waarden op deze punt is hoger dan die van de afgelopen meting    # ^^ een top, waarden rechts en links zijn kleiner
        peak = True
    ChangeValueInProcent = changeInProcent
    return peak
#lst=[]
lst=[1,2,3,4,5,10,5,3,2,1,2,1,5,5,4,3,5,5,6,6,7,8,8,5,6,5,7,5,4,4,5,3,2,1,2,3,1,2,1,2,1,0,2,3,4,5,3,5,7,6,7,8,7,9,11,12,15,20,30,20,15,12,16,12,10,12,10,4,10,18,1,0,0,0,0,0,0,0,0]

# for i in range(0,100):
#     n = random.random() * 10
#     lst.append(n)

ChangeValueInProcent = 0

MaLst = []
MaLst.append(lst[0])
MaLst.append(lst[1])
MaLst.append(lst[2])
MaLst.append(lst[3])

for i in range(4,len(lst),1):
    MA = (lst[i] + lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4]) / 5
    MaLst.append(MA)

measurements=[]
for i in range(0,len(lst),1):
    measurements.append(i)



peaksx=[]
peaksy=[]
for i in range(1,len(lst)-1,1):
    if(detectAPeak(lst[i-1],lst[i],lst[i+1])):
        peaksx.append(i)
        peaksy.append((lst[i] + 5))

if len(peaksx) > 0:
    for i in range(0,len(peaksx)):
        plt.plot(peaksx[i], peaksy[i], 'h')

plt.plot(measurements,lst, label = "strength")
plt.plot(measurements,MaLst, label = "Moving average(5)")#, linestyle="-.")
plt.title("heartbeatplot")
plt.xlabel("time/measurements")
plt.ylabel("heartbeatstrength")
plt.legend()
plt.show()
