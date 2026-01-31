#solemne 1
import numpy as np
import matplotlib.pyplot as plt

sig = 10.0
r = 28.0
b = 8.0/3.0

x_0, y_0, z_0 = 0.0, 1.0, 0.0 #condiciones iniciales

t_0 = 0.0 #tiempo inicial
t_f = 50.0 #tiempo final
h= 0.01
N = int((t_f - t_0)/h)
t = np.linspace(t_0, t_f, N+1)

def f(x, y, z, t):
  dx = sig * (y - x)
  dy = r*x - y - x*z
  dz = x*y - b*z
  return dx, dy, dz

def rk4_step(x, y, z, t, h):
  k1x, k1y, k1z = f(x,y,z,t)
  k2x, k2y, k2z = f(x+0.5*h*k1x, y+0.5*h*k1y, z+0.5*h*k1z, t +0.5*h)
  k3x, k3y, k3z = f(x+0.5*h*k2x, y+0.5*h*k2y, z+0.5*h*k2z, t +0.5*h)
  k4x, k4y, k4z = f(x+h*k3x, y+h*k3y, z+h*k3z, t+h)

  x_n = x+(h/6.0)*(k1x + 2*k2x + 2*k3x +k4x)
  y_n = y+(h/6.0)*(k1y + 2*k2y + 2*k3y + k4y)
  z_n = z+(h/6.0)*(k1z + 2*k2z + 2*k3z + k4z)
  return x_n, y_n, z_n

X = np.zeros(N+1)
Y = np.zeros(N+1)
Z = np.zeros(N+1)
X[0] = x_0
Y[0] = y_0
Z[0] = z_0

x = x_0
y = y_0
z = z_0

for i in range(N):
    x, y, z = rk4_step(x, y, z, t[i], h)
    X[i+1], Y[i+1], Z[i+1] = x, y, z

plt.figure(figsize=(8, 4))
plt.figure()
plt.plot(t, Y, "-b")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Lorentz y(t)")


plt.figure(figsize=(8, 4))
plt.figure()
plt.plot(X, Z, 'red', linewidth = "0.8")
plt.xlabel("x")
plt.ylabel("z")
plt.title("Strange attractor")

plt.show()











