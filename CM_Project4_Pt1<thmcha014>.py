#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 5 12:15:05 2020
Module: AST40007W-Computaional Methods 
#Shooting Method Project.  
@author: Chad Thomas <thmcha014>
"""

#Importing packages.
import numpy as np 
import matplotlib.pyplot as plt 

#------------------------------------------------------------------------------
#generate your own data set from a function with a non-constant
#second derivative
#------------------------------------------------------------------------------

time = np.linspace(0,0.5,100)        #Time (s) 
pos = time**3 + time**2              #Position.
vel = 3*time**2 + 2*time             #Velocity.
acc = 6*time + 2                     #acccccceleration.

fig, ax = plt.subplots(1,3, sharex = True, figsize = (17, 5))

ax[0].plot(time, pos, 'o')
ax[0].set_xlabel('Time (s)', size = 20)
ax[0].set_ylabel('Position (m)', size = 20)
ax[0].set_title('Position (m) vs Time (s)', size = 20)

ax[1].plot(time, vel, 'o')
ax[1].set_xlabel('Time (s)', size = 20)
ax[1].set_ylabel('Velocity (m.s^-1)', size = 20)
ax[1].set_title('Velocity (m.s^-1) vs Time (s)', size = 20)

ax[2].plot(time, acc, 'o')
ax[2].set_xlabel('Time (s)', size = 20)
ax[2].set_ylabel('Acceleration (m.s^-2)', size = 20)
ax[2].set_title('Acceleration (m.s^-2) vs Time (s)', size = 20)

#------------------------------------------------------------------------------
#Intergrating over the generated data to check if our intergration techniques,
#are working correctly and given the correct output. 
#------------------------------------------------------------------------------

#Setting initial values. 
v0 = vel[0]
y0 = pos[0]

#Creating an empty array to store the velocity values and initial value. 
v_values    = np.zeros(time.shape)
y_values    = np.zeros(time.shape)
v_values[0] = v0
y_values[0] = y0 

#------------------------Intergrating Acceleration-----------------------------

#Defining the trapezoidal rule. 
def trapezoidal(x, pos):
    return 0.5*(x[i] - x[i-1])*(pos[i-1] + pos[i])

#Creating for loop to run over each generated data point. 
for i in range (1,time.size): 
    v_values[i] = v_values[i-1] + trapezoidal(time,acc)
   

#------------------------Intergrating Velocity---------------------------------

for i in range (1,time.size): 
    y_values[i] = y_values[i-1] + trapezoidal(time,v_values)


#---------------------------Plotting Results-----------------------------------

fig, ax = plt.subplots(1,2, sharex = True, figsize = (17, 5))

#Position vs Time 
ax[0].plot(time, pos, 'o', label='Manuel intergration result')
ax[0].plot(time, y_values, 'k--', label = 'Intergration technique result', color ='red', linewidth=3)
ax[0].set_xlabel('Time (s)', size = 20)
ax[0].set_ylabel('Position (m)', size = 20)
ax[0].set_title('Position (m) vs Time (s)', size = 20)
ax[0].legend(loc="upper left")

#Velocity vs Time 
ax[1].plot(time, vel, 'o', label='Manuel intergration result')
ax[1].plot(time, v_values, 'k--', label = 'Intergration technique result', color ='red', linewidth=3)
ax[1].set_xlabel('Time (s)', size = 20)
ax[1].set_ylabel('Velocity (m.s^-1)', size = 20)
ax[1].set_title('Velocity (m.s^-1) vs Time (s)', size = 20)
ax[1].legend(loc="upper left")

plt.show()

#------------------------------------------------------------------------------
#---------------------------------END------------------------------------------
#------------------------------------------------------------------------------

































