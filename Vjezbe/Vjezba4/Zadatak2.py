import math
import matplotlib.pyplot as plt
import numpy as np
from particle import Particle

v0=10
theta=60
g=9.81
ad = (v0**2 * math.sin(math.radians(2 * theta)))/g
dt_vrijednosti= np.linspace(0.001, 0.1, 100)
Err= []

for dt in dt_vrijednosti:
    p = Particle(v0, theta)
    nd = p.range(dt)
    err = abs((nd-ad)/ad)
    Err.append(err)

plt.figure(figsize=(10,8))
plt.plot(dt_vrijednosti, Err)
plt.xlabel('dt [s]')
plt.ylabel('Relativna pogreška')
plt.show()
