from scipy.stats import maxwell
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = maxwell.stats(moments='mvsk')
x = np.linspace(maxwell.ppf(0.01), maxwell.ppf(0.99), 10000)
ax.plot(x, maxwell.pdf(x),'r-', lw=5.5, alpha=0.6)
vals = maxwell.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], maxwell.cdf(vals))
r = maxwell.rvs(size=1000)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
print(mean,var,skew,kurt)