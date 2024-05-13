# Problem 1
import numpy as np
import matplotlib.pyplot as plt
#------------------------------defining the given function
def f(x):
    if(x==0):
        return 1
    else:
        return np.sin(x)/x
x=np.linspace(-10,10,100)
D=(max(x)-min(x))/float(len(x))
y=[]
for i in range(len(x)):
    y.append(f(x[i]))
#------------------------------   
p=np.fft.fftfreq(len(x),d=D) 
p=2*np.pi*p
p=np.fft.fftshift(p)
phase=np.exp(-1j*p*min(x))
f1=np.fft.fft(y,norm='ortho')*D*np.sqrt(len(x)/(2*np.pi))*phase
f1=np.fft.fftshift(f1) 
#---------------------
def Analytic(x): 
        return 0.5*np.sqrt(np.pi*0.5)*(np.sign(1-x)+np.sign(1+x))
Ya=[]
for i in range(len(x)):
    Ya.append(Analytic(x[i]))
    
plt.plot(x,Ya,label='Analytic')    
plt.plot(p,f1.real,'-',label="Numerical")   
#plt.plot(x,y,label="Actual function")
plt.xlim(-5,5)
plt.grid()
plt.legend()
plt.show()