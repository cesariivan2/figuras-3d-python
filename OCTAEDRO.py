import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

A = (2, 2, 4)
B = (2, 2, 0)

C = (0, 2, 2)
D = (4, 2, 2)

E = (2, 0, 2)
F = (2, 4, 2)

vertices = [A, B, C, D, E, F]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LAS CARAS
# ============================

caras = [
    [A, C, E],
    [A, E, D],
    [A, D, F],
    [A, F, C],

    [B, C, E],
    [B, E, D],
    [B, D, F],
    [B, F, C]
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

for nombre, vertice in zip(
    ["A", "B", "C", "D", "E", "F"],
    vertices
):

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
    (A, C),
    (A, D),
    (A, E),
    (A, F),

    (B, C),
    (B, D),
    (B, E),
    (B, F),

    (C, E),
    (E, D),
    (D, F),
    (F, C)
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
ax.set_ylim(-1, 5)
ax.set_zlim(-1, 5)

ax.set_box_aspect([1, 1, 1])

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Octaedro formado por vértices, aristas y caras"
)

plt.show()