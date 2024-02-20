import vxi11
import time
from pylab import *
import sys
from numpy import *

ip=sys.argv[1]
sa = vxi11.Instrument(str(ip))

fmin=0
fmax=7100000000 #ogranicenje uredjaja
rlev=-50
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
sa.write(':detector:negative') #tip detektora
time.sleep(0.3)

n=10000
f=linspace(fmin,fmax,n)
A=[]
for el in f:
	sa.write(':calculate:marker:X '+str(el))
	time.sleep(0.2)
	Y=float(sa.ask(':calculate:marker:Y?'))
	A.append(Y)

ops=[]
for el in range(len(A)):
	if A[el] > (max(A)-3): 
		ops.append(f[el])
		
print('Propusni ospeg je ['+str(ops[0])+','+str(ops[-1])+']')
A=array(A)
plot(f,A)
title('Amplitudska karakteristika')
sa.close()
show()
