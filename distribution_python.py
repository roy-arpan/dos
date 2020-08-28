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


x=pow(10,-7)*(random.rand(10))
y=numpy.sqrt(x)
y=y*1j
# print(numpy.complex(0,y))
print(y)

b=numpy.zeros([2])

print(b)
# clc
# clear all
# I=10e-3;    %laser power
# E0=sqrt(I);     %field amplitude
# neff=1.45;  %effective refractive index of mode
# c=3e8;      % velocity of light in vaccum
# v=c/neff;   % velocity of light in fibre
# LPW=1e-6;   % Laser pulse width in time domain
# W=LPW*v;    % laser pulse width in space
# M=1000;     % number of reflector for any instant
# % Mx=rand(1,M);  % M random value
# L=20000;     % length of the fibre in meter
# T=2*(L/v);      % time required to travel the fibre length
# t=LPW:1e-7:(T/2); % different time position for signal accusition
# % r=1e-6;      % reflactance at every point "for this problen it is consider as constant
# alpha=0.17e-3; % in dB/m
# l=length(t);
# z=v*t-(W/2);     % position of pulse in different time position
# zavg=v*t-(W/4);
# lamda=1.55e-6;
# wa=(2*pi)/lamda;
# for i=1:1:l
#     Mx=rand(1,M);
#     r=sqrt(1e-7*rand(1,M));
#     rposi=z(i)+(W/2)*Mx;
#     phi=((4*pi*neff)/lamda)*rposi;
#     k=r.*exp(1i.*phi);
#     s(i)=sum(k);
#     Eb(i)=E0*exp(-2*alpha*zavg(i))*exp(1i*wa*2*t(i))*s(i);
# end
# x=(abs(Eb)).^2;
# plot(z,x)

# for i in range ()
# c=3e8;
# L=1000; %length of the fibre
# l=10; % each component
# % n=1000/10; 
# M=1000;
# z=1:1:10000;
# n=length(z);
# lamda=1550e-9;
# w=(2*pi*c)/lamda;
# T=z./c;
# r=1e-7;
# for k=1:1:n
#     tot=0;
#     for j=1:1:M
#         x=(z(k)-0.5)+(1/M)*j*rand;
#         pa=(4*pi*1.44*x)/lamda;
#         tot=tot+exp(1i*(pa));
#     end
#     a=w*2*T(k);
#     E(k)=(abs(exp(-2*0.00019*z(k))*exp(1i*a)*tot));
# end
# plot(z,E)