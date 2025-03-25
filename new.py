import matplotlib.pyplot as plt
import numpy as np

# ডেটা সেট তৈরি করা
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Subplot 1: Line Plot with Markers
plt.subplot(2, 1, 1)  # 2 row, 1 column এর মধ্যে প্রথম subplot
plt.plot(x, y1, marker='o', color='blue', label='Sine Wave')  # sine graph with markers
plt.plot(x, y2, marker='x', color='red', label='Cosine Wave')  # cosine graph with markers
plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  # গ্রিড যোগ করা
plt.legend()  # লিজেন্ড যোগ করা

# Subplot 2: Scatter Plot
plt.subplot(2, 1, 2)  # 2 row, 1 column এর মধ্যে দ্বিতীয় subplot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
plt.scatter(x_scatter, y_scatter, color='green', marker='^', label='Random Points')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  # গ্রিড যোগ করা
plt.legend()  # লিজেন্ড যোগ করা

# প্রদর্শন করা
plt.tight_layout()  # layout adjust করা
plt.show()
