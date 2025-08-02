import math
import matplotlib.pyplot as plt

def f1(n):
    return n * math.log2(n)

def f2(n):
    return n ** 1.5

ns = [2**k for k in range(1, 11)]
vals1 = [f1(n) for n in ns]
vals2 = [f2(n) for n in ns]

plt.plot(ns, vals1, marker='o', label='n log n')
plt.plot(ns, vals2, marker='x', label='n^1.5')
plt.xlabel('n')
plt.ylabel('Function value')
plt.title('Growth rate comparison')
plt.legend()
plt.grid(True)
plt.show()
