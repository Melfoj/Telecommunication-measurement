import vxi11
import time
from pylab import *

osc = vxi11.Instrument('10.200.100.2')
fg = vxi11.Instrument('10.200.100.5')

s='sin'
f=1000
Vpp=2
fmin=200
fmax=3000
n=150
fg.write('appl:'+s)
time.sleep(0.3)
fg.write('freq '+str(f))
time.sleep(0.3)
fg.write('volt '+str(Vpp))
time.sleep(0.3)
fg.write('outp1 on')
time.sleep(0.3)
osc.write('aut')
time.sleep(5)
fq=linspace(fmin,fmax,n)
A=[]
ch1=[]
ch2=[]
for el in fq:
	fg.write('freq '+str(el))
	time.sleep(0.3)
	Vch1=float(osc.ask('meas:vpp? chan1'))
	ch1.append(Vch1)
	Vch2=float(osc.ask('meas:vpp? chan2'))
	ch2.append(Vch2)
	A.append(20*log10(Vch2/Vch1))

ops=[]
for el in range(len(A)):
	if A[el] > (max(A)-3): 
		ops.append(fq[el])
		
print('Propusni ospeg je ['+str(ops[0])+','+str(ops[-1])+']')
A=array(A)
ch1=array(ch1)
ch2=array(ch2)
plot(fq,A)
title('Amplitudska karakteristika')
osc.close()
fg.close()
show()
