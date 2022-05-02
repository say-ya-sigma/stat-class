import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3.0, 3.0, 100)
y = x**2
plt.plot(x, y)
plt.savefig('stat_class/chapter1/sample.png')
