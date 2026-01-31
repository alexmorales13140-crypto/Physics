import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
exp= np.exp
# parte 1
def newton_index(z0, n):
    # raíces de la unidad
    roots = [exp(2*pi*1j*m/n) for m in range(n)]

    z = z0
    for k in range(100):
        # Newton-Rhapson
        z = z - (z**n - 1) / (n * z**(n-1))

        # chequeo de convergencia
        for m, root in enumerate(roots):
            if abs(z - root) < 0.1:
                return m # índice de la raíz encontrada
    return 0 # no convergió
#parte 2
def newton_indices_grid(n=3, N=1001):
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y

    roots = np.exp(2j*np.pi*np.arange(n)/n)
    M = np.zeros((N, N), dtype=int)
    conv = np.zeros((N, N), dtype=bool)

    for _ in range(100):
        mask = ~conv
        if not np.any(mask):
            break
        Zm = Z[mask]
        Z[mask] = Zm - (Zm**n - 1) / (n * Zm**(n-1) + 1e-12)

        for m, root in enumerate(roots):
            cerca = (np.abs(Z - root) < 0.1) & (~conv)
            M[cerca] = m
            conv[cerca] = True

    return x, y, M

# ejemplo con n=3
x, y, M = newton_indices_grid(3, 1001)

#parte 3

def newton_indices_grid(n=3, N=1001):
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y

    roots = np.exp(2j*np.pi*np.arange(n)/n)
    M = np.zeros((N, N), dtype=int)
    conv = np.zeros((N, N), dtype=bool)

    for _ in range(100):
        mask = ~conv
        if not np.any(mask):
            break
        Zm = Z[mask]
        Z[mask] = Zm - (Zm**n - 1) / (n * Zm**(n-1) + 1e-12)

        for m, root in enumerate(roots):
            cerca = (np.abs(Z - root) < 0.1) & (~conv)
            M[cerca] = m
            conv[cerca] = True

    return x, y, M

# Graficar para n=3,4,5
for n in [3, 4, 5]:
    x, y, M = newton_indices_grid(n=n, N=1001)
    plt.figure(figsize=(6, 6))
    plt.imshow(M, extent=[x.min(), x.max(), y.min(), y.max()],
               origin='lower', interpolation='nearest', cmap='tab10')
    plt.title(f'Fractal de Newton para n={n}')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    cbar = plt.colorbar(ticks=range(n))
    cbar.set_label('índice m')
    plt.tight_layout()
    plt.show()

#parte 4
def newton_steps_grid(n=3, N=1001):
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j*Y

    roots = np.exp(2j*np.pi*np.arange(n)/n)
    steps = np.zeros((N, N), dtype=int)
    conv = np.zeros((N, N), dtype=bool)

    for k in range(1, 101):
        mask = ~conv
        if not np.any(mask):
            break
        Zm = Z[mask]
        Z[mask] = Zm - (Zm**n - 1) / (n * Zm**(n-1) + 1e-12)

        for root in roots:
            cerca = (np.abs(Z - root) < 0.1) & (~conv)
            steps[cerca] = k
            conv[cerca] = True

    return x, y, steps

# Graficar para n=3,4,5
for n in [3, 4, 5]:
    x, y, steps = newton_steps_grid(n=n, N=1001)
    plt.figure(figsize=(6, 6))
    plt.imshow(steps, extent=[x.min(), x.max(), y.min(), y.max()],
               origin='lower', interpolation='nearest', cmap='inferno')
    plt.title(f'Número de pasos hasta convergencia (n={n})')
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    cbar = plt.colorbar()
    cbar.set_label('Pasos')
    plt.tight_layout()
    plt.show()