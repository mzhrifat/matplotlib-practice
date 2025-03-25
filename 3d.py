
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ডেটা সেট তৈরি করা
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# 3D প্লট তৈরি করা
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3D Scatter plot
ax.scatter(x, y, z, color='red')

# শিরোনাম এবং লেবেল যোগ করা
ax.set_title('3D Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# গ্রাফ দেখানো
plt.show()
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ডেটা সেট তৈরি করা
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))  # 3D সাইন ফাংশন

# 3D প্লট তৈরি করা
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3D সাফল্য গ্রাফ আঁকা
ax.plot_surface(x, y, z, cmap='viridis')  # Surface plot

# শিরোনাম এবং লেবেল যোগ করা
ax.set_title('3D Surface Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# গ্রাফ দেখানো
plt.show()
