# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:23:53 2016

@author: owendix
"""

from math import sqrt, pi, tan, sin, cos, asin
import scipy as sp


def earthRadMi(lat):
    #Earth's semi major axis, miles    
    a = 3963.1906
    #Earth's semi minor axis miles
    b = 3949.9028
    
    c = a*cos(lat)
    s = b*sin(lat)
    
    return sqrt(((a*c)**2 + (b*s)**2)/(c**2 + s**2))
    
def dAngHaversine(lat1,lat2,dLon):
    #not for use with lat1, lat2 antipodal: small angle only
    #it is being applied to the Earth, after all
    dLat = abs(lat2-lat1)
    dLon = abs(dLon)
    
    return 2*asin(sqrt(sin(dLat/2.)**2 + cos(lat1)*cos(lat2)*sin(dLon/2.)**2))

#gps coordinates of end point (lat, lon)
e = sp.array([35.328006,-111.689625])*pi/180.
#gps coordinates of start point (lat, lon)
s = sp.array([35.326275,-111.686261])*pi/180.
#start height
sh = 11450
#end height
eh = 10775

#radius of the earth to lowest point in feet
Re = earthRadMi((e[0]+s[0])/2.)*5280 + eh

dLon = e[1] - s[1]

dAng = dAngHaversine(s[0],e[0],abs(dLon))

#this method gives a lower limit of the sliding distance since a straight
#line is the shortest path but the slope angle probably varied
#base of triangle: horizontal distance traveled during slide in feet
d_base = Re*dAng
#height of triangle: elevation change during slide in feet
h = sh - eh
#675
#hypotenuse of triangle: lower limit for sliding distance in feet
d_slide = sqrt(h**2 + d_base**2)
#1537.107321441536
#average angle of slope in degrees
ang_slope = tan(h/d_base)*180/pi
#sliding distance in miles
#0.29111881087907876
#approximate sliding time 1 minute: convert to hours
#assume constant acceleration (ignores wind resistance)
#this overestimates the max speed:
#if it approaches terminal velocity for a person, estimate is less accurate
#far from terminal velocity, estimate is more accurate
#v_max = 2*(d_slide/5280)*60
print('minimum distance slid (feet):',d_slide)
print('minimum distance slid (miles):',d_slide/5280)
print('average angle of slope (deg):',ang_slope)
