from pylab import *
from numpy import NaN
from numpy import arange, zeros
import matplotlib.pyplot as plt

def m(a):
    z = 0
    for n in range(1, 100):
        z = z**4 + a
        if abs(z) > 2:
            return n
    return NaN

X = arange(-2, .5, .001)
Y = arange(-1,  1, .001)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
    print (iy, "of", len(Y))
    for ix, x in enumerate(X):
        Z[iy,ix] = m(x + 1j * y)

plt.imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.savefig("mandelbrot_python.svg")
plt.show()
