"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data create kora
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Figure and axis create kora
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Update function define kora, jeta har frame er jonno call hobe
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # y-data ke update kora
    return line,

# Animation create kora
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show animation
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data create kora
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Figure and axis create kora
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Update function define kora, jeta har frame er jonno call hobe
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # y-data ke update kora
    return line,

# Animation create kora
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show animation
plt.show()
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Random image data create kora
image_data = np.random.rand(10, 10)

# Figure and axis create kora
fig, ax = plt.subplots()

# Initial image plot kora
img = ax.imshow(image_data, cmap='gray')

# Update function, jeta har frame e image update korbe
def update(frame):
    new_data = np.random.rand(10, 10)  # New random data generate kora
    img.set_data(new_data)  # Image-er data update kora
    return img,

# Animation create kora
ani = FuncAnimation(fig, update, frames=range(100), interval=200)

# Show animation
plt.show()
