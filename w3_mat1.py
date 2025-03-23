"""

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '3')
plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,8,1,10])
plt.plot(y,'o-.',marker='s',mec='r',mfc='r')
plt.show()