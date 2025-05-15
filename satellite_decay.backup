import numpy as np
import matplotlib.pyplot as plt

# Constants
R_earth = 6371e3  # meters
mu = 3.986e14     # m^3/s^2
Cd = 2.2          # drag coefficient
A = 4.0           # cross-sectional area (m^2)
m = 1120          # mass of satellite (kg)

# Atmospheric density model (simplified exponential)
def rho(h):
    return 1.225 * np.exp(-h / 8500)

# Simulation
dt = 60  # time step in seconds
t_max = 365 * 24 * 3600  # simulate 1 year

h = 250e3  # initial altitude (m)
v = np.sqrt(mu / (R_earth + h))
t = 0

time = []
altitude = []

while h > 120e3 and t < t_max:
    v = np.sqrt(mu / (R_earth + h))
    drag = 0.5 * rho(h) * v**2 * Cd * A / m
    dh = drag * dt
    h -= dh
    t += dt
    time.append(t / 3600 / 24)  # in days
    altitude.append(h / 1000)   # in km

# Plot
plt.plot(time, altitude)
plt.title("Orbital Decay Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Altitude (km)")
plt.grid()
plt.savefig("img/altitude_vs_time.png")
plt.show()
