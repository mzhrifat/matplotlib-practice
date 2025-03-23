"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the Axes.
ax.set_ylabel('y label')  # Add a y-label to the Axes.
ax.set_title("Simple Plot")  # Add a title to the Axes.
ax.legend()  # Add a legend.
plt.show()  # Display the figure.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # উদাহরণ ডেটা।

plt.figure(figsize=(5, 2.7))  # ফিগার তৈরি করুন।
plt.plot(x, x, label='Linear')  # কিছু ডেটা প্লট করুন।
plt.plot(x, x**2, label='Quardat')  # আরও ডেটা প্লট করুন...
plt.plot(x, x**3, label='CUBIC')  # ... এবং আরও কিছু।
plt.xlabel('x Today')  # x-লেবেল যোগ করুন।
plt.ylabel('y now')  # y-লেবেল যোগ করুন।
plt.title("Time")  # শিরোনাম যোগ করুন।
plt.legend()  # লেজেন্ড যোগ করুন।
plt.show()  # ফিগারটি প্রদর্শন করুন।

