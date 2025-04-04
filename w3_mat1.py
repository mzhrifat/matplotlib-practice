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


#color each dot

import matplotlib.pyplot as plt
import numpy as np

#x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
#colors =np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
#comormap
#colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
#plt.scatter(x,y,c=colors)

#plt.scatter(x,y,c=colors, cmap='viridis')
#colorbar and comormap add
#plt.colorbar()

#size add
#sizes= np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#plt.scatter(x,y,s=sizes)

#add alpha
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))

colors=np.random.randint(100,size=(100))
sizes=10* np.random.randint(100,size=(100))

plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()

plt.show()

#BARS
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([4,8,2,10])

#plt.bar(x,y)

#add color
#plt.bar(x,y,color="red")

#horizontal line
#plt.barh(x,y)

#add width
#plt.bar(x,y,width=0.2)

#add height

#plt.barh(x,y,height=0.1)

#ADD color,width,height,horizontal

plt.barh(x,y,color="green",height=0.1,)
plt.bar(x,y,color="green",width=0.2)

plt.show()

#HISTOGRAM COMMT

import matplotlib.pyplot as plt
import numpy as np

# Data set up (উদাহরণস্বরূপ র‍্যান্ডম ডেটা)
data = np.random.randn(10)

# Histogram plot করা
plt.hist(data, bins=10, color='blue', edgecolor='black')

# Title এবং labels যুক্ত করা
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot দেখানো
plt.show()
"""

#Multiople histogram in one plot
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)* 1.5 + 2
y=np.random.randn(100) * 0.5 + 1

plt.hist(x,bins=30,color='green',edgecolor='red')
plt.hist(y,bins=5 ,color='hotpink',edgecolor='blue')

plt.title("Multiple Histogram ")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()