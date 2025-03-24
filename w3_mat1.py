"""

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '3')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,8,1,10])
plt.plot(y,marker='s',ms=20,mec='y',mfc='y',linestyle='-.',color='r',linewidth='20')
plt.show()



#multiple line
import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])

plt.plot(x1, y1, marker='o', ms=10, mec='y', mfc='y', color='r', linewidth=2,linestyle='--')  # প্রথম লাইন
plt.plot(x2, y2, marker='s', ms=10, mec='b', mfc='b', color='g', linewidth=2,linestyle='-.')  # দ্বিতীয় লাইন

plt.title("Multiple line",)
plt.xlabel("SPORTS")
plt.ylabel("sCORE")
plt.show()

#labels and lines

import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])

font1={'family': 'serif','color': 'blue','size': 20}
font2={'family': 'serif','color': 'darkred','size': 15}

#plt.plot(x1, y1, marker='o', ms=10, mec='y', mfc='y', color='r', linewidth=2,linestyle='--')  # প্রথম লাইন

plt.title("Multiple line",fontdict=font1,loc='left')

plt.xlabel("SPORTS", fontdict= font2)

plt.ylabel("sCORE", fontdict=font2)
plt.plot(x1,y1)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])

font1={'family': 'serif','color': 'blue','size': 20}
font2={'family': 'serif','color': 'darkred','size': 15}

#plt.plot(x1, y1, marker='o', ms=10, mec='y', mfc='y', color='r', linewidth=2,linestyle='--')  # প্রথম লাইন

plt.title("Multiple line",fontdict=font1,loc='left')

plt.xlabel("SPORTS", fontdict= font2)

plt.ylabel("sCORE", fontdict=font2)
plt.plot(x1,y1)
plt.grid(axis='y',linestyle='--',linewidth=0.5,color='r')
plt.show()




#subplot
#column
import matplotlib.pyplot as plt
import numpy as np

#plot1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Incomes")

#plot2
x=np.array([0,1,2,3])
y=np.array([10,12,14,15])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Sales")

plt.suptitle("Daily")
plt.show()

#row

import matplotlib.pyplot as plt
import numpy as np

#plot1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("Incomes")

#plot2
x=np.array([0,1,2,3])
y=np.array([10,12,14,15])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.title("Sales")
plt.suptitle("Daily")
plt.show()


#SCATTER

import matplotlib.pyplot as plt
import numpy as np
#plot1
#day one,the age, and speed of the (n)cars
x=np.array([5,7,8,7,2,17])
y=np.array([99,86,87,88,111,86])

#plt.scatter(x,y)
#add color
plt.scatter(x,y,color='hotpink')

#plot2
#day two,the age,and speed of the cars
x=np.array([2,3,6,1,8])
y=np.array([20,22,25,28,30])

#plt.scatter(x,y)
#add color
plt.scatter(x,y,color='green')
plt.show()
"""

#color each dot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors =np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x,y,c=colors)
plt.show()


