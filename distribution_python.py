# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:25:57 2020

@author: Arpan
"""


# import matplotlib
# print(matplotlib.__version__)

from matplotlib import pyplot as plt

# plt.show()

import math
import cmath
import numpy

from numpy import random

I=100*pow(10,-3)    #laser power
E0=math.sqrt(I)     #field amplitude
neff=1.45      #effective refractive index of mode
c=3*pow(10,8) #velocity of light
v=c//neff     # velocity of light in fibre

pw=pow(10,-6)   # Laser pulse width in time domain
W=pw*v         # laser pulse width in space
M=1000        # number of reflector for any instant
L=10000        #length of the fibre
T=2*(L/v)      # time required to travel the fibre length
p=int(T//pow(10,-7))
t=numpy.linspace(pw,T,p)  #different time position for signal accusition
alpha=0.17*pow(10,-3)  # in dB/m
l=len(t)          # different time position for signal accusition
z=numpy.linspace(1,11,10)
# n=len(z)
z=v*t-(W/2)     # position of pulse in different time position
zavg=v*t-(W/4)
pi=(22/7)
lamda=1550*pow(10,-9)
wa=(2*pi)/lamda
s=numpy.zeros(l)
Eb=numpy.zeros(l)

for i in range(0,l,1):
    Mx=(random.rand(M))
    r=numpy.sqrt(pow(10,-7)*(random.rand(M)))
    rposi=z[i]+(W/2)*Mx
    phi=(((4*pi*neff)/lamda)*rposi)*1j
    phi=numpy.exp(phi)
    k=numpy.multiply(r, phi)
    s[i]=sum(k)
    Eb[i]=E0*(numpy.exp(-2*alpha*zavg[i]))*(numpy.exp((wa*2*t[i])*1j))*s[i]

x=numpy.square((Eb))
plt.plot(z,x)
plt.show()

