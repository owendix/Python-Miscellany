# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:37:53 2016

A shorter ski allows snow drifts to exert a smaller torque 
on the foot, but also have a lesser rotational inertia.

Assumes an equal area supporting the skier as the length shrinks, 
which is not actually true. The effect of the smaller rotational 
inertia is neglible for reasonable values (~0.5-10%).

@author: owendix
"""
import scipy as sp
import matplotlib.pyplot as plt

ang_a=1.0
#ang_as = sp.arange(0.,1.01,0.5)
F_fric = 100.
#range of fraction the effective moment arm of friction force is of total
#ski length L
cs = sp.arange(0.2,0.501,0.15)
m = 4.  #kg
#1.6m * 0.15m (length x width approx)
A = 1.6*0.12

L = sp.arange(0.8,1.7,0.02)
w = A/L
I = (1./12.)*m*(L**2 + w**2)
T_fric0 = L*F_fric
#plt.plot(L,w)

for c in cs:
    Trq_ext = c*L*F_fric
    Trq_foot = Trq_ext + I*ang_a
    plt.plot(L,Trq_foot, 
        label='c='+str(c)+'L')

plt.title('c: moment arm of outside force; effect of I negligible')
plt.legend(loc='best')     
plt.xlabel('Ski length (m)')
plt.ylabel('Torque by foot rel. to outside force (%)')
plt.grid()
plt.show()     
