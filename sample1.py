import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500)
f=100;
f2=250;
fs=10000;
s=0.5*np.cos(2*np.pi*f/fs*n+np.pi/2)
plt.subplot(211)
plt.stem(n,s);plt.show()
s1=0.5*np.cos(2*np.pi*f/fs*n+np.pi/2)
plt.subplot(212)
plt.stem(n,s1);plt.show()
z=s+s1
plt.stem(n,z);plt.show()
