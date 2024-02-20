from pylab import *
from scipy.signal import *
x1=[]
f=open('lab6.txt','r')
x = f.read()
f.close()
x=x.replace(':',';')
x=x.split(';')
u = x[0]
x=x[1:-1]
for el in x:
	x1.append(float(el))

t=range(0,len(x1))
T1=1/60
t=[(el/len(x1))*T1*1000 for el in t]
plot(t,x1)
xlabel("t[ms]")
ylabel(u)
show()
X=fftshift(abs(fft(x)))
X=[(a/max(X))*0.7 for a in X]
A=find_peaks(X,prominence=0.3-1)
P=0
for a in A[0]:
        P+=(X[a]*X[a])

print('P='+ str(round(P,3)))
S=0
h1=X[A[0][int(len(A[0])/2)]]
for a in A[0]:
        if a>len(X)/2:
                S+=X[a]**2
S=S-(h1*h1)
thd=sqrt(S)/h1
print('thd=' + str(round(thd,3)))
