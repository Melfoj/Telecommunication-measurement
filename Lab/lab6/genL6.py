from pylab import *
a = 'v1[V]:'
f1 = 60
f2 = 3*f1
t = linspace(0,1/f1, 120)
s = 1.4*cos(2*pi*f1*t)-0.3*sin(2*pi*f2*t)

for sample in s:
  a+=(str(sample)+';')

a = a[:-1]
a+=':end\n'

f = open('lab6.txt', 'w', encoding = 'utf-8')
f.write(a)
f.close()