import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,5,100)
y=5*x+np.random.normal(loc=0, scale=25, size=len(x))
a=np.linspace(3.5,6.5,50.0)
pravci=np.zeros(len(x),len(a))


for i in range(len(a)):
    pravci[:,i]=x*a[i]
plt.figure()
plt.scatter(x,y)
plt.plot(x,a*x, 'k')
plt.show()
