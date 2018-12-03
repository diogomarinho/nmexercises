# how to use newton bisec fsolve and root
from scipy.optimize import newton, bisect, fsolve, root
f = lambda x: 2*x**2 - 5*x + 3
print('{:2f}'.format(newton(f, 0)))
print('{:2f}'.format(bisect(f, 1.1, 1.8)))
print(fsolve(f, 0))
print(root(f, 0))
