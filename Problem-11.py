# Problem-11  convolution
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    if(x<1 and x>-1):
        return 1
    else:
        return 0
#-----------values of actual function at different x points
x=np.linspace(-5,5,1000)
G=[]
for i in range(len(x)):
    G.append(f(x[i]))
#------------convolution
x=list(x)
dx=abs(x[1]-x[0])
y=x[0]
Y=[]
F=[]
I=0
for j in range(len(x)):
    p=0
    for i in range(len(x)):
        p+=f(x[i])*f(y-x[i])*dx
    F.append(p)
    #print(F)
    Y.append(y)
    y+=dx
    I+=1

plt.plot(x,G,label="Actual function") # plotting the given function
plt.plot(Y,F,label="convolution") #plotting the convoluted function
plt.legend()
plt.grid()
plt.show()