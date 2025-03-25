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
plt.show()