#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:34:38 2020
Module: AST40007W-Computaional Methods 
#Shooting Method Project.  
@author: Chad Thomas <thmcha014>
"""
#Importing packages.
import numpy as np 
import matplotlib.pyplot as plt 

#Reading the data file given. 
data = np.loadtxt('project4_data.csv', delimiter = ',', skiprows = 1)

#Assigning time, acceleration and interval values from the data set given. 
time = data[:,0]               #Time (s).
acc = data[:,1]              #Acceleration (m/s^2).

#Initial conditions
y0   = 0                    #Initial position.  
v0   = 0                    #Initial velocity.

#Creating an empty array to store the velocity values and initial value. 
v_values    = np.zeros(time.shape)
y_values    = np.zeros(time.shape)
v_values[0] = v0
y_values[0] = y0 

#------------------------Intergrating Acceleration-----------------------------
#Defining the trapezoidal rule. 
def trapezoidal(x, y):
    return 0.5*(x[i] - x[i-1])*(y[i-1] + y[i])

for i in range (1,time.size): 
    v_values[i] = v_values[i-1] + trapezoidal(time,acc)

#------------------------Intergrating Velocity---------------------------------

for i in range (1,time.size): 
    y_values[i] = y_values[i-1] + trapezoidal(time,v_values)

#---------------------------Plotting results-----------------------------------


#Position vs Time 
plt.plot(time, y_values, 'o', linewidth=2)
plt.xlabel('Time (s)', size = 13)
plt.ylabel('Position (m)', size = 13)
plt.title('Position (m) vs Time (s)', size = 15)
plt.show()

#Velocity vs Time 
plt.plot(time, v_values, 'o', linewidth=2)
plt.xlabel('Time (s)', size = 13)
plt.ylabel('Velocity (m.s^-1)', size = 13)
plt.title('Velocity (m.s^-1) vs Time (s)', size = 15)
plt.show()

#Acceleration vs Time
plt.plot(time, acc, 'o', linewidth=2)
plt.xlabel('Time (s)', size = 13)
plt.ylabel('Acceleration (m.s^-2)', size = 13)
plt.title('Acceleration (m.s^-2) vs Time (s)', size = 15)
plt.show()

#------------------------------------------------------------------------------
#Determining the maximum height and determining the time interval when the
#rockets runs out of water. 
#------------------------------------------------------------------------------

print (np.max(y_values))

for i in range (1,time.size):
    if y_values[i] == np.max(y_values):
        print('The rocket achieves a maximum height of ', y_values[i],' at a time of ', time[i],' seconds')


for i in range (1,time.size):
    if acc[i] == np.max(acc):
        print('The rocket runs out of water between ', time[i],' seconds and  ', time[i+1],' seconds')

















