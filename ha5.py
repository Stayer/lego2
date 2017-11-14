
# coding: utf-8

# In[150]:

import csv
import numpy as np

b = 0.125
r = 0.027

xl = list()
yl = list()
ol = list()
s1 = list()
x_cur = 0
y_cur = 0
o_cur = 0
with open('Experiment.csv', newline='') as csvfile:
# with open('Downloads/Homework_Sis_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    items = list(spamreader)
#     i = 0
    for i in range(0, len(items)):
#         print(items[i])
        if i < 2:
            continue

        sl = float(items[i][4])-float(items[i-1][4]) # left delta
        sr = float(items[i][5])-float(items[i-1][5]) # right delta
#         o  = float(row[3])-float(items[i-1][3]) # angle 
#         tetta = 
        print(sl,sr,o_cur)
#         sl = float(row[4])-float(items[i-1][4]) # left delta
#         sr = float(row[5])-float(items[i-1][5]) # right delta
#         o = float(row[3]) # angle 
        
        x_cur = x_cur + (sr + sl)/2*np.cos(o_cur +((sr-sl)/(2*b)))
        y_cur = y_cur + (sr + sl)/2*np.sin(o_cur +((sr-sl)/(2*b)))
        o_cur = o_cur + (sr-sl)/b
        
        xl.append(x_cur)
        yl.append(y_cur)
        ol.append(o_cur)
        s1.append(float(items[i][2])-45.4)
#         i+=1
        
        # print(', '.join(row))


# In[151]:

import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 10, 0.005)
# y = np.exp(-x/2.) * np.sin(2*np.pi*x)
# print(yl)
x = xl
y = yl
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(x, y)
# plt.plot(xl, yl, 'r') # plotting t, a separately 
# plt.plot(s1, yl, 'b') # plotting t, b separately 
# plt.plot(t, c, 'g') # plotting t, c separately 
# plt.show()
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 1)

# plt.show()


# In[152]:

import math

zero_distance = 0

channel = []
row_replacement = None
sonar_list = s1
angle_list = ol
i = 0
# print(angle_list)
for row_index in sonar_list:
    if row_replacement is not None:
        y = row_replacement(sonar_list[i], angle_list[i])
    else:
        y = sonar_list[i] *math.cos(angle_list[i])
    i+=1
    channel.append(y - zero_distance)

# np.multiply(channel, -1)
# print(channel)


# In[153]:

plt.plot(xl, yl, 'r') # plotting t, a separately 
plt.plot(channel, yl, 'b') # plotting t, b separately 
plt.plot(xl, s1, 'g') # plotting t, c separately 
plt.show()


# In[ ]:



