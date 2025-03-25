import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import title

sizes=([35,25,10,30])

mylabels=["Apples","Bananas","Cherries","Dates"]

#also add angles(startangles)
#ADD Explode
myexplode=[0.2,0.1,0.1,0.1]

mycolors=["black","green","hotpink","b"]
#add shadow
#plt.pie(x,labels=mylabels,startangle=90,explode=myexplode)

#plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow=True)

#add colors
plt.pie(sizes,labels=mylabels,startangle=90,explode=myexplode,shadow=True,autopct='%1.1f%%',colors=mycolors)
plt.legend(title= "Four Fruits",loc="best")
plt.axis('equal')
plt.show()