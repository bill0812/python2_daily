import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
a = np.array([2, 4, 1, 2, 3, 2])
res = stats.relfreq(a, numbins=6)
print res.frequency
