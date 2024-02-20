import matplotlib.pylab as py
x1=[]
f=open('dz5proba.txt','r')
x = f.read()
f.close()
x=x.replace(':',';')
x=x.split(';')
Tb = float(x[1])
u = x[2]
x=x[3:-1]
for el in x:
	x1.append(float(el))

TbN=range(0,len(x1)) 
TbN = [int(el) * Tb/len(x1) for el in TbN]
py.plot(TbN,x1)
py.xlabel("t [s]")
py.ylabel(u)
py.show()
