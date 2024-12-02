import numpy as np
import matplotlib.pyplot as plt
from sympy import *

target = 1

r = abs(target)
phi = np.angle(target)

n = 8
roots = [r ** (1 / 8) * np.exp(1j * (phi + 2 * np.pi * k) / n) for k in range(n)]

x = [z.real for z in roots]
y = [z.imag for z in roots]

plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=0.5, linestyle='-')
plt.axvline(0, color='black', linewidth=0.5, linestyle='-')
plt.scatter(x, y, color="red")
plt.grid(color="gray", linestyle="-", linewidth=0.5)
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()