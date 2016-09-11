# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:38:41 2015

Hot Wheels Car Jump -> ramp to ground below table
Predict horizontal displacement from ramp

@author: owendix
"""
import numpy as np
import matplotlib.pyplot as plt
theta=15    #degrees
theta *= np.pi/180
            #now in radians

g = 9.81    #m/s^2
m = 0.031   #m  mass of the car

hR = 0.06  #m  height of the ramp, including center of mass shift of the car
hT = 0.75  #m

hTotal = hR + hT

hT2Stop = 0.105 #m  height of car's CM until it halts at the top of the ramp


#print('initial height\t dx with Friction\t dx w/o Friction\t Diff from Fric')

#for hI in np.arange(0.25,0.9,0.01):
hI = np.arange(0.25,0.85,0.01)
   
#Magnitude, from conservation of energy
#With and Without Friction, respectively
vJFric = np.sqrt(np.multiply(2*g,np.subtract(hI,hT2Stop)))
vJ0Fric = np.sqrt(np.multiply(2*g,np.subtract(hI,hR)))

#Components
#With Friction
vJFricX = np.multiply(vJFric,np.cos(theta))
vJFricY = np.multiply(vJFric,np.sin(theta))
#No Friction    
vJ0FricX = np.multiply(vJ0Fric,np.cos(theta))
vJ0FricY = np.multiply(vJ0Fric,np.sin(theta))

#Constants for calculating horizontal displacement
tauFric = np.divide(vJFricY,g)
tau0Fric = np.divide(vJ0FricY,g)
tH = 2*hTotal/g    

#Horizontal displacement, w & w/o fric, respectively
termFric = np.sqrt(np.add(np.power(tauFric,2.0),tH))
term0Fric = np.sqrt(np.add(np.power(tau0Fric,2.0),tH))

dxFric = np.multiply(vJFricX,np.add(tauFric,termFric))
dx0Fric = np.multiply(vJ0FricX,np.add(tau0Fric,term0Fric))

#print(hI,'m: \t', dxFric, 'm, \t', dx0Fric, 'm\t', dx0Fric - dxFric, 'm')
plt.xlabel('Car\'s Initial Height above Table (m)')
plt.ylabel('$d_x$ fm Ramp (m) %0.2f m above ground' % hTotal)
plt.text(0.50,1.6,'w/o Friction')
plt.text(0.55,1.25,'w/ Friction')
plt.grid(True)
plt.plot(hI,dxFric,'r--',hI,dx0Fric,'b-')

plt.show()

    
    
