# Problem 6
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft,fftfreq

def f(x):
        return 1
x=np.linspace(-10,10,1000)
y=[]
for i in range(len(x)):
    y.append(f(x[i]))
#------------------------------   
p=fftfreq(len(x)) 
f1=fft(y)
plt.subplot(212)
plt.grid()
plt.plot(p,abs(f1),label="Fourier transformed function") 
plt.title("Fourier transformed function")
plt.subplot(211)  
plt.plot(x,y,label="Actual function")
#plt.xlim(-2.5,2.5)
#plt.plot(x,(F),label="Inv FT of the FT")
plt.grid()
plt.legend()
plt.show()
