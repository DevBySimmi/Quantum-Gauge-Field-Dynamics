import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================================
# Quantum Gauge Field Dynamics
# =====================================

LATTICE_SIZE = 10

# Grid
x, y = np.meshgrid(
    np.arange(LATTICE_SIZE),
    np.arange(LATTICE_SIZE)
)

# Initial phase field
phi = np.random.uniform(
    0,
    2 * np.pi,
    (LATTICE_SIZE, LATTICE_SIZE)
)

# Figure setup
fig, ax = plt.subplots(figsize=(8, 8))

fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# Clean styling
ax.set_title(
    "Quantum Gauge Field Dynamics",
    fontsize=20,
    color="white",
    pad=20
)

ax.set_xlabel("x", color="white")
ax.set_ylabel("y", color="white")

ax.tick_params(colors="white")

ax.grid(
    color="white",
    alpha=0.08,
    linestyle="--"
)

ax.set_aspect("equal")

ax.set_xlim(-0.5, LATTICE_SIZE - 0.5)
ax.set_ylim(-0.5, LATTICE_SIZE - 0.5)

# Gauge field
gauge_field = np.exp(1j * phi)

U = np.real(gauge_field)
V = np.imag(gauge_field)

# Main arrows
quiver = ax.quiver(
    x,
    y,
    U,
    V,
    color="#ff6ec7",   # Neon pink
    scale=5,
    width=0.006,
    headwidth=4,
    headlength=5
)

# Small subtitle
subtitle = ax.text(
    0.5,
    1.02,
    "Lattice Gauge Field Simulation",
    transform=ax.transAxes,
    ha="center",
    color="#66ffff",
    fontsize=11
)

# =====================================
# Animation
# =====================================

def update(frame):

    global phi

    # Smooth evolving field
    phi += 0.08 * (
        np.sin(x * 0.6 + frame * 0.08)
        + np.cos(y * 0.6 + frame * 0.08)
    )

    gauge_field = np.exp(1j * phi)

    U = np.real(gauge_field)
    V = np.imag(gauge_field)

    quiver.set_UVC(U, V)

    return quiver,

# Create animation
ani = FuncAnimation(
    fig,
    update,
    frames=500,
    interval=40,
    blit=False
)

plt.tight_layout()
plt.show()