"""
#A simple pie
import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,35,15,15])
plt.pie(x)
plt.show()
"""

#labels
import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,10,30])

mylabels=["Apples","Bananas","Cherries","Dates"]
plt.pie(x,labels=mylabels)
plt.show()