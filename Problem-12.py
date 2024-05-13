#Problem 12
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x**2)
def h(x):
    return np.exp(-4*x**2)
#-----------Analytic solution
x=np.linspace(-5,5,1000)
D=(max(x)-min(x))/len(x)
def Analytic(x):
    return np.sqrt(np.pi/5.0)*np.exp(-(4.0/5.0)*x**2)
G=[]
for i in range(len(x)):
    G.append(Analytic(x[i]))
    
#------------convolution(numerical)

f=f(x)
h=h(x)
Ff=np.fft.fft(f)
Fh=np.fft.fft(h)
conv=Ff*Fh*D
F_conv=np.fft.ifft(conv)
F_conv=np.fft.fftshift(F_conv)



plt.plot(x,G,label="Analytic") # plotting the given function
plt.grid()
plt.plot(x,F_conv.real,label='numerical')
plt.legend()
plt.show()