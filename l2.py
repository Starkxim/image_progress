import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *
import sympy

'''
# 2.1
x = np.linspace(-5, 2, 100)
y1 = x ** 3 + 5 * x ** 2 + 10
y2 = 3 * x ** 2 + 10 * x
y3 = 6 * x + 10
fig, ax = plt.subplots()
ax.plot(x, y1, color='blue', label='y(x)')
ax.plot(x, y2, color='red', label='y`(x)')
ax.plot(x, y3, color='green', label='y``(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
fig.savefig('l2_1.png')
plt.show()
'''

'''
# 2.2
fig = plt.figure(figsize=(8, 2.5), facecolor='#f1f1f1')
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height], facecolor='#e1e1e1')
x = np.linspace(-2, 2, 1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x ** 2)
ax.plot(x, y1 * y2)
ax.plot(x, y2, 'g')
ax.plot(x, -y2, 'g')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.savefig('graph1.png', dpi=500, facecolor='#f1f1f1')
plt.show()
'''

'''
# 2.3
sym_x = sympy.Symbol('x')
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)


def sin_expansion(x, n):
    return sympy.lambdify(sym_x, sympy.sin(sym_x).series(n=n + 1).removeO(), 'numpy')(x)


fig, ax = plt.subplots()
ax.plot(x, np.sin(x), linewidth=4, color='red', label='exact')
colors = ['blue', 'black']
linestyles = [':', '-.', '--']
for idx, n in enumerate(range(1, 12, 2)):
    ax.plot(x, sin_expansion(x, n), color=colors[idx // 3], linestyle=linestyles[idx % 3], linewidth=3,
            label='order %d approx.' % (n + 1))
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(-1.5 * np.pi, 1.5 * np.pi)
ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.0)
fig.subplots_adjust(right=0.75)
fig.savefig('l2_3.png')
plt.show()
'''

'''
# 2.4
# axis labels and titles
x = np.linspace(0, 30, 500)
y = np.sin(x) * np.exp(-x / 10)
fig, axes = plt.subplots(1, 3, figsize=(9, 3), subplot_kw={'facecolor': '#ebf5ff'})

axes[0].plot(x, y, lw=2)
axes[0].set_xlim(-5, 35)
axes[0].set_ylim(-1, 1)
axes[0].set_title('set_xlim/set_ylim')

axes[1].plot(x, y, lw=2)
axes[1].axis('tight')
axes[1].set_title('axis("tight")')

axes[2].plot(x, y, lw=2)
axes[2].axis('equal')
axes[2].set_title('axis("equal")')

fig.savefig('l2_4.png')
plt.show()
'''

'''
# 2.5
# ticks
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y = np.sin(x) * np.exp(-x ** 2 / 20)
fig, axes = plt.subplots(1, 4, figsize=(12, 3))

axes[0].plot(x, y, lw=2)
axes[0].set_title('default ticks')

axes[1].plot(x, y, lw=2)
axes[1].set_title('set_xticks')
axes[1].set_xticks([-5, 0, 5])
axes[1].set_yticks([-1, 0, 1])

axes[2].plot(x, y, lw=2)
axes[2].set_title('set_mojar_locator')
axes[2].xaxis.set_major_locator(mpl.ticker.MaxNLocator(4))
axes[2].yaxis.set_major_locator(mpl.ticker.FixedLocator([-1, 0, 1]))
axes[2].xaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))
axes[2].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(8))

axes[3].plot(x, y, lw=2)
axes[3].set_title('set_xticklabels')
axes[3].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
axes[3].set_yticks([-1, 0, 1])
axes[3].set_xticklabels([r'$-2\pi$', r'$-\pi$', 0, r'$\pi$', r'$2\pi$'])
x_minor_ticker = mpl.ticker.FixedLocator([-3 * np.pi / 2, -np.pi / 2, 0, np.pi / 2, 3 * np.pi / 2])
axes[3].xaxis.set_minor_locator(x_minor_ticker)
axes[3].yaxis.set_minor_locator(mpl.ticker.MaxNLocator(4))

fig.savefig('ticks.png')
plt.show()
'''

'''
# 2.6
# grid lines
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y = np.sin(x) * np.exp(-x ** 2 / 20)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
x_major_ticker = mpl.ticker.MultipleLocator(4)
x_minor_ticker = mpl.ticker.MultipleLocator(1)
y_major_ticker = mpl.ticker.MultipleLocator(0.5)
y_minor_ticker = mpl.ticker.MultipleLocator(0.25)
for ax in axes:
    ax.xaxis.set_major_locator(x_major_ticker)
    ax.xaxis.set_minor_locator(x_minor_ticker)
    ax.yaxis.set_major_locator(y_major_ticker)
    ax.yaxis.set_minor_locator(y_minor_ticker)
    ax.plot(x, y, lw=2)

axes[0].set_title('default grid')
axes[0].grid()

axes[1].set_title('major/minor grid')
axes[1].grid(which='both', color='blue', linestyle=':', linewidth=0.5)

axes[2].set_title('individual x/y major/minor grid')
axes[2].grid(which='major', axis='x', color='red', linestyle='-', linewidth=0.5)
axes[2].grid(which='minor', axis='x', color='green', linestyle=':', linewidth=0.25)
axes[2].grid(which='major', axis='y', color='black', linestyle='-', linewidth=0.5)

fig.savefig('grid.png')
plt.show()
'''