import vxi11
import time
from pylab import *

sa = vxi11.Instrument('147.91.9.239')

fmin=10000
fmax=100000
rlev=0
pdv=10
Bv=10
Br=10

sa.write(':frequency:start '+str(fmin))#Start freq
time.sleep(0.3)
sa.write(':frequency:stop '+str(fmax))#Stop freq
time.sleep(0.3)
sa.write(':display:window:trace:Y:rlevel '+str(rlev))#Referentni nivo
time.sleep(0.3)
sa.write(':display:window:trace:Y:pdivision '+str(pdv))#Razmer
time.sleep(0.3)
sa.write(':bandwidth:video '+str(Bv))#Propusni opseg video filra
time.sleep(0.3)
sa.write(':bandwidth:resolution '+str(Br))#Propusni opseg rezolucionog filtra
time.sleep(0.3)

n=200
fq=linspace(fmin,fmax,n)
A=[]
for el in fq:
	sa.write(':calculate:marker:X '+str(el))
	time.sleep(0.3)
	Y=float(sa.ask(':calculate:marker:Y?'))
	A.append(Y)

ops=[]
for el in range(len(A)):
	if A[el] > (max(A)-3): 
		ops.append(fq[el])
		
print('Propusni ospeg je ['+str(ops[0])+','+str(ops[-1])+']')
A=array(A)
plot(fq,A)
title('Amplitudska karakteristika')
sa.close()
show()
