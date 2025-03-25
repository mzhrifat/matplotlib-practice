"""
#A simple pie
import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,35,15,15])
plt.pie(x)
plt.show()
"""
"""
#labels
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import title

x=np.array([35,25,10,30])

mylabels=["Apples","Bananas","Cherries","Dates"]

#also add angles(startangles)
#ADD Explode
myexplode=[0.2,0.1,0.1,0.1]

mycolors=["black","green","hotpink","b"]
#add shadow
#plt.pie(x,labels=mylabels,startangle=90,explode=myexplode)

#plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow=True)

#add colors
plt.pie(x,labels=mylabels,startangle=90,explode=myexplode,shadow=True,colors=mycolors)
plt.legend(title= "Four Fruits")
plt.show()

"""


import matplotlib.pyplot as plt

# ডেটা সেট তৈরি করা
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']  # প্রতিটি সেকশনের নাম
sizes = [25, 35, 20, 20]  # প্রতিটি সেকশনের মান
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # রংগুলোর তালিকা

# Pie Chart তৈরি করা
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Legend যুক্ত করা
plt.legend(labels, loc="best")

# Plot দেখানো
plt.axis('equal')  # Pie Chart কে গোলাকার দেখানোর জন্য সমান অক্ষ (equal axis) ব্যবহার করা
plt.show()
