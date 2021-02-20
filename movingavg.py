from scipy.io import wavefile
import numpy as np
y=10*np.random.rand(10)
z=np.zeros(len(y))
m=int(input('enter order'))
for n in range(0,len(y)):
	for k in range(0,m):
	s=0.0-
	q=[]
	if n-k>=0:
		q.append(y[n-k])
		s=s+y[n-k]
	z[n]=s/m
print(y)
print(z)
plt.subplot(211)
plt.stem(y)
	
