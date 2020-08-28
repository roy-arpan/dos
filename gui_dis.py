from tkinter import *
from matplotlib import pyplot as plt
import math
import cmath
import numpy
from numpy import random

window=Tk()

window.geometry("500x350")
window.config(background="#09BEAD")
window.title("Trace for DOF sensor")

Label(window, text="Input power", font=("times", 15, "bold"), bg="#09BEAD", fg="black").place(x=17, y=30)
Power_entry = Entry(window, bg="white", fg="black", font=("Times New Roman", 18))
Power_entry.insert(0, "in mW")
Power_entry.place(x=140, y=30, width=150, height=25)

Label(window, text="Pulse width", font=("times", 15, "bold"), bg="#09BEAD", fg="black").place(x=17, y=60)
pulse_entry = Entry(window, bg="white", fg="black", font=("Times New Roman", 18))
pulse_entry.insert(0, "in mu meter")
pulse_entry.place(x=140, y=60, width=150, height=25)

Label(window, text="Fibre length", font=("times", 15, "bold"), bg="#09BEAD", fg="black").place(x=17, y=90)
flen_entry = Entry(window, bg="white", fg="black", font=("Times New Roman", 18))
flen_entry.insert(0, "in meter")
flen_entry.place(x=140, y=90, width=150, height=25)

Label(window, text="No. of reflector in each pulse length", font=("times", 15, "bold"), bg="#09BEAD", fg="black").place(x=17, y=120)
ref_entry = Entry(window, bg="white", fg="black", font=("Times New Roman", 18))
ref_entry.insert(0, "1000")
ref_entry.place(x=325, y=120, width=150, height=25)

def trace():
    #I=100*pow(10,-3)    #laser power
    I=float(Power_entry.get())
    I=I*pow(10,-3)    #laser power
    E0=math.sqrt(I)     #field amplitude
    neff=1.45      #effective refractive index of mode
    c=3*pow(10,8) #velocity of light
    v=c//neff     # velocity of light in fibre
    pw=float(pulse_entry.get())
    pw=pw*pow(10,-6)   # Laser pulse width in time domain
    W=pw*v         # laser pulse width in space
    M=1000        # number of reflector for any instant
    L=float(flen_entry.get())        #length of the fibre
    T=2*(L/v)      # time required to travel the fibre length
    p=int(T//(2*pow(10,-7)))
    t=numpy.linspace(pw,(T/2),p)  #different time position for signal accusition
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

showTrace = Button(window,text="Show trace", command=trace)
showTrace.place(x=200,y=160)
Button(window,text="Quit", command=window.quit).place(x=300,y=300, width=60)
window.mainloop()