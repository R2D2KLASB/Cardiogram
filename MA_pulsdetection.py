import random
import numpy as np
from matplotlib import pyplot as plt
from skimage import feature
from scipy.ndimage.filters import maximum_filter


lst=[]
lst=[1,2,3,4,6,12,6,3,2,1,2,1,5,5,4,3,5,5,6,6,7,20,8,5,6,5,7,5,4,4,5,3,2,1,2,3,1,2,1,2,1,0,2,3,4,5,3,5,7,6,7,8,7,9,11,12,15,20,30,20,15,12,16,12,10,12,10,4,10,18,1,0,0,0,0,0,0,0,0]
#
# for i in range(0,100):
#     n = random.random() * 10
#     lst.append(n)

MaLst = []
MaLst.append(lst[0])
MaLst.append(lst[1])
MaLst.append(lst[2])
MaLst.append(lst[3])

for i in range(4, len(lst), 1):
    MA = (lst[i] + lst[i-1] + lst[i-2] + lst[i-3] + lst[i-4]) / 5
    MaLst.append(MA)

measurements=[]
for i in range(0,len(lst),1):
    measurements.append(i)

plt.plot(measurements,MaLst, label = "Moving average(5)")#, linestyle="-.")

# put your data here
data = np.array(lst)

filter_win_size = 12
peak_intensity_threshold = 5

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

# fig, ax = plt.subplots()
r = range(data.shape[0])
plt.plot(r, data, 'k')
plt.plot(max_places, data[max_places], 'xr')
plt.grid()
plt.axis((0, 100, 0, 12))
plt.show()
