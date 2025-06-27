import numpy as np
import matplotlib.pyplot as plt

# Lorentzova sila
def lorentzova_sila(naboj, E, B, brzina):
    return naboj * (E + np.cross(brzina, B))

# Eulerova metoda
def simuliraj_euler(masa, naboj, pocetno_stanje, E, B, dt, trajanje):
    stanje = np.array(pocetno_stanje, dtype=float)
    x, y, z = [stanje[0]], [stanje[1]], [stanje[2]]
    vrijeme = np.arange(0, trajanje, dt)

    for _ in vrijeme:
        brzina = stanje[3:]
        F = lorentzova_sila(naboj, E, B, brzina)
        a = F / masa
        stanje[3:] += a * dt
        stanje[:3] += stanje[3:] * dt
        x.append(stanje[0])
        y.append(stanje[1])
        z.append(stanje[2])

    return np.array(x), np.array(y), np.array(z)

# Runge-Kutta metoda (4. reda)
def simuliraj_rk4(masa, naboj, pocetno_stanje, E, B, dt, trajanje):
    stanje = np.array(pocetno_stanje, dtype=float)
    x, y, z = [stanje[0]], [stanje[1]], [stanje[2]]
    vrijeme = np.arange(0, trajanje, dt)

    def derivacije(stanje):
        pozicija = stanje[:3]
        brzina = stanje[3:]
        a = lorentzova_sila(naboj, E, B, brzina) / masa
        return np.concatenate((brzina, a))

    for _ in vrijeme:
        k1 = derivacije(stanje)
        k2 = derivacije(stanje + 0.5 * dt * k1)
        k3 = derivacije(stanje + 0.5 * dt * k2)
        k4 = derivacije(stanje + dt * k3)
        stanje += (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        x.append(stanje[0])
        y.append(stanje[1])
        z.append(stanje[2])

    return np.array(x), np.array(y), np.array(z)

# Prikaz dviju putanja u jednom 3D prikazu
def prikazi_usporedbu_3d(x1, y1, z1, x2, y2, z2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x1, y1, z1, label='Euler')
    ax.plot(x2, y2, z2, label='Runge-Kutta')
    ax.set_title("Usporedba putanja (elektron)")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# Graf razlike u poziciji
def prikazi_razliku(x1, y1, z1, x2, y2, z2, dt):
    udaljenosti = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    vrijeme = np.arange(0, dt * len(udaljenosti), dt)
    plt.plot(vrijeme, udaljenosti)
    plt.title("Razlika pozicije između Euler i Runge-Kutta")
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Udaljenost (m)")
    plt.grid()
    plt.show()


# Parametri
masa_e = 1
q_e = -1
pocetno_stanje_e = [0, 0, 0, 0.1, 0.1, 0.1]
E = np.array([0, 0, 0])
B = np.array([0, 0, 1])
dt = 0.01
trajanje = 10

# Simulacije
x_e_euler, y_e_euler, z_e_euler = simuliraj_euler(masa_e, q_e, pocetno_stanje_e, E, B, dt, trajanje)
x_e_rk4, y_e_rk4, z_e_rk4 = simuliraj_rk4(masa_e, q_e, pocetno_stanje_e, E, B, dt, trajanje)

# Prikazi rezultate
prikazi_usporedbu_3d(x_e_euler, y_e_euler, z_e_euler, x_e_rk4, y_e_rk4, z_e_rk4)
prikazi_razliku(x_e_euler, y_e_euler, z_e_euler, x_e_rk4, y_e_rk4, z_e_rk4, dt)
