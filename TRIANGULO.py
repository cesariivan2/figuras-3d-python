import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

A = (0, 0, 0)
B = (4, 0, 0)
C = (2, 2, 3)
E = (0, 4 ,0)
F = (4, 4, 0)
vertices = [A, B, C, E, F]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LA CARA
# ============================
caras = [
    [A, B, F, E],  # base
    [A, B, C],     # cara frontal
    [B, F, C],     # cara derecha
    [F, E, C],     # cara trasera
    [E, A, C]      # cara izquierda
]

figura = Poly3DCollection(
    caras,
    alpha=0.4,
    edgecolor="black"
)

ax.add_collection3d(figura)



# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================

for nombre, vertice in zip(["A", "B", "C", "E", "F"], vertices):

    x, y, z = vertice

    ax.scatter(x, y, z, s=80)

    ax.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================

aristas = [
    (A, B),
    (B, C), 
    (C, E),
    (E, A),
    (A, C),
    (B, F),
    (F, C),
    (F, E),
    ]


for inicio, fin in aristas:

    ax.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)
ax.set_zlim(-1, 2)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Triángulo formado por vértices, aristas y 5 caras"
)

plt.show()