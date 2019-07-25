import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

def wrap(r,x,N):
    holder = []
    def compute(r, x, N):
        if N ==1:

            return r*x*(1-x)
            # print('exhausted')
        else:
            current = r*x*(1-x)
#             print(f'{N}:{current}')
            holder.append(current)
            return compute(r, current, N-1)
    compute(r,x,N)
    if holder[-1] == holder[-2]:
        return holder[-1]
    else:
        return holder[-200:]


L = [float(j) for j in list(np.linspace(2,8,75))]

y = [wrap(i, 0.5, 990) for i in L]



base = [[j,k] for i, (j,k) in enumerate(zip(L, y)) if type(y[i])!=list]

extra = [[j,k] for i, (j,k) in enumerate(zip(L, y)) if type(y[i])==list]

A = [a for [a, b] in base]
B = [b for [a, b] in base]
# A2 = [a for [a, b] in extra]
# B2 = [b for [a, b] in extra]



plt.plot(A[:-1], B[:-1])
plt.plot(A2,B2)
plt.xlabel(r'$\lambda$')
plt.ylabel(r'X$_{N = 990}$')
plt.title(r'Logistic Map Plot'+'\n'+r'$X_{n+1} = \lambda \bullet X_{n}(1- X_{n})$')

plt.show()
