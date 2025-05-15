import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
R_earth = 6371e3  # Earth radius (m)
mu = 3.986e14     # Earth gravitational parameter (m^3/s^2)
Cd = 2.2          # Drag coefficient
A = 4.0           # Cross-sectional area (m^2)
m = 1120          # Satellite mass (kg)

# Atmospheric density (simplified exponential)
def rho(h):
    return 1.225 * np.exp(-h / 8500)

# Initial orbit parameters
h0 = 250e3          # Initial altitude (m)
r0 = R_earth + h0   # Initial orbit radius (m)

# Time step and total simulation time
dt = 60             # seconds
t_max = 365 * 24 * 3600  # 1 year in seconds

# Calculate orbital velocity for circular orbit
def orbital_velocity(r):
    return np.sqrt(mu / r)

# Set up figure and 3D axis
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(projection='3d')

# Draw Earth as a sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_earth = R_earth * np.outer(np.cos(u), np.sin(v))
y_earth = R_earth * np.outer(np.sin(u), np.sin(v))
z_earth = R_earth * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_earth, y_earth, z_earth, color='b', alpha=0.3)

# Initialize orbit radius and position angle
r = r0
theta = 0

# Satellite marker
satellite, = ax.plot([], [], [], 'ro', markersize=6)

# Set axis limits and labels
ax.set_xlim([-r0*1.2, r0*1.2])
ax.set_ylim([-r0*1.2, r0*1.2])
ax.set_zlim([-r0*1.2, r0*1.2])
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Satellite Orbit with Orbital Decay')

# Variables for decay calculation
t = 0

def update(frame):
    global r, theta, t

    v = orbital_velocity(r)
    alt = r - R_earth
    drag_accel = 0.5 * rho(alt) * v**2 * Cd * A / m
    dr = drag_accel * dt
    r -= dr

    omega = v / r
    theta += omega * dt

    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = 0

    satellite.set_data([x], [y])
    satellite.set_3d_properties(z)

    t += dt

    if alt < 120e3:
        anim.event_source.stop()

    return satellite,


# Create animation
anim = FuncAnimation(fig, update, frames=int(t_max/dt), interval=50, blit=True)

plt.show()
