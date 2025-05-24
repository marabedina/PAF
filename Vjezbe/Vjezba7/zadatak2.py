import matplotlib.pyplot as plt
from Projectile import projectile  
x0, y0 = 0, 0
v0 = 50
kut = 45
masa = 1
otpor = 0.1
dt = 0.01


projektil1 = projectile(x0, y0, v0, kut, masa, otpor, dt)
x_euler, y_euler = projektil1.euler_simulacija()

projektil2 = projectile(x0, y0, v0, kut, masa, otpor, dt)
x_rk, y_rk = projektil2.rk4_simulacija()


plt.plot(x_euler, y_euler, label='Eulerova metoda')
plt.plot(x_rk, y_rk, label='Runge-Kutta 4. reda')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Putanja projektila')
plt.legend()

plt.show()