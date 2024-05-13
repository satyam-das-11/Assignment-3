# Problem-10
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft,fftfreq
x=np.linspace(-5,5,70)
y=np.linspace(-5,5,70)
D=(max(x)-min(x))/len(x)
#---------------the given function
def F(x,y):
    return np.exp(-(x**2+y**2))


fig = plt.figure()
#ax=plt.axes(projection='3d')
ax = fig.add_subplot(1,2,1, projection='3d')

#---------------let's construct the mesh-grid on (x,y) plane
xg,yg=np.meshgrid(x,y)
func=F(xg,yg)
I=len(xg) 
J=len(xg[0])
X,Y,Z=[],[],[]
for i in range(I):
    for j in range(J):
        X.append(xg[i][j])
        Y.append(yg[i][j])
        Z.append(func[i][j])
plt.title("The given function")
ax.plot3D(X,Y,Z,'green')

#-------------meshgrid on the fourier space
kx=np.fft.fftfreq(len(x),D)
kx=np.fft.fftshift(kx)
ky=np.fft.fftfreq(len(y),D)
ky=np.fft.fftshift(ky)
kx=2*np.pi*kx
ky=2*np.pi*ky
kx,ky=np.meshgrid(kx,ky)

func_f=np.fft.fft2(func,norm="ortho")
func_f=np.fft.fftshift(func_f)

Kx,Ky,Kz=[],[],[]
for i in range(I):
    for j in range(J):
        Kx.append(kx[i][j])
        Ky.append(ky[i][j])
        Kz.append(func_f[i][j])
Kz_analytic=[]
#--------------------------
#Analytic solution
def Analytic(kx,ky):
    return 0.5*np.exp(-0.25*(kx**2+ky**2))
Kx=np.array(Kx)
Ky=np.array(Ky)
for i in range(len(Kx)):
    Kz_analytic.append(Analytic(Kx[i],Ky[i]))    
#--------------------------
#numerical solution
phase=np.exp(-1j*Kx*min(x)-1j*Ky*min(y))
Kz=np.array(Kz)*(D)**2 *np.sqrt(len(x)/(2*np.pi))**2 *phase        # because FT(f(r))=(D)^n*D/np.sqrt(2pi)^n*( phase)*DFT(f(r))
                                                             # where n=dimension

ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot3D(Kx,Ky, Kz_analytic,'blue',label="Analytic")
ax.plot3D(Kx,Ky,Kz.real,'red',label="Numerical")
plt.title("The function in the fourier space")
plt.legend()
plt.show()