import matplotlib.pyplot as plt
import numpy as np

sizes=([15,30,45,10])

mylabels=["Apples","Bananas","Cherries","Dates"]

myexplode=[0.2,0.1,0.1,0.1]

mycolors=["yellowgreen","green","hotpink","lightskyblue"]

plt.pie(sizes,labels=mylabels,explode=myexplode,autopct='%1.1f%%',colors=mycolors,shadow=True)

plt.legend(title="four fruits",loc="best")

plt.axis('equal')
plt.show()